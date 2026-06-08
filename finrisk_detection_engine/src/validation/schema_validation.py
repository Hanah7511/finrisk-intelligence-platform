from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Dict, List

import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Validation Report

@dataclass
class ValidationReport:
    passed: bool = True
    missing_columns: List[str] = field(default_factory=list)
    type_mismatches: Dict[str, str] = field(default_factory=dict)
    missing_value_counts: Dict[str, int] = field(default_factory=dict)
    duplicate_row_count: int = 0
    duplicate_payment_id_count: int = 0
    invalid_value_checks: Dict[str, int] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def summary(self) -> None:
        print("\n--- Validation Report ----------------------")
        print(f"Status                : {'PASSED' if self.passed else 'FAILED'}")
        print(f"Missing cols          : {self.missing_columns or 'None'}")
        print(f"Type issues           : {self.type_mismatches or 'None'}")
        print(f"Missing values        : {self.missing_value_counts or 'None'}")
        print(f"Duplicate rows        : {self.duplicate_row_count}")
        print(f"Duplicate payment_id  : {self.duplicate_payment_id_count}")
        print(f"Invalid value checks  : {self.invalid_value_checks or 'None'}")
        if self.errors:
            print("Errors:")
            for e in self.errors:
                print(f"  - {e}")
        print("-------------------------------------------\n")


# Expected Schema

EXPECTED_COLUMNS: List[str] = [
    "payment_id",
    "order_id",
    "customer_id",
    "account_age_days",
    "kyc_level",
    "customer_risk_segment",
    "repeated_beneficiary_flag",
    "device_id",
    "ip_risk_score",
    "device_shared_flag",
    "payment_status",
    "payment_timestamp",
    "payment_method",
    "transaction_channel",
    "geo_risk_level",
    "transaction_direction",
    "counterparty_country",
    "instrument_age_days",
    "transaction_hour",
    "amount_usd_equivalent",
    "velocity_score",
    "amount_risk_score",
    "device_risk_score",
    "transaction_frequency_24h",
    "transaction_frequency_7d",
    "geo_mismatch_flag",
    "sanctions_country_flag",
    "high_risk_corridor_flag",
    "structuring_flag",
    "fraud_label",
    "item_count",
    "total_quantity",
    "unique_products",
    "unique_merchants",
    "max_product_risk_score",
    "avg_product_risk_score",
    "customer_txn_count_30d",
    "customer_avg_amount_30d",
    "customer_unique_devices_30d",
    "customer_unique_countries_30d",
    "customer_unique_merchants_30d",
    "customer_failed_payments_7d",
    "new_device_flag",
    "new_country_flag",
]

EXPECTED_TYPES: Dict[str, str] = {
    "payment_id": "numeric",
    "order_id": "numeric",
    "customer_id": "numeric",
    "account_age_days": "numeric",
    "kyc_level": "string",
    "customer_risk_segment": "string",
    "repeated_beneficiary_flag": "numeric",
    "device_id": "string",
    "ip_risk_score": "numeric",
    "device_shared_flag": "numeric",
    "payment_status": "string",
    "payment_timestamp": "datetime",
    "payment_method": "string",
    "transaction_channel": "string",
    "geo_risk_level": "string",
    "transaction_direction": "string",
    "counterparty_country": "string",
    "instrument_age_days": "numeric",
    "transaction_hour": "numeric",
    "amount_usd_equivalent": "numeric",
    "velocity_score": "numeric",
    "amount_risk_score": "numeric",
    "device_risk_score": "numeric",
    "transaction_frequency_24h": "numeric",
    "transaction_frequency_7d": "numeric",
    "geo_mismatch_flag": "numeric",
    "sanctions_country_flag": "numeric",
    "high_risk_corridor_flag": "numeric",
    "structuring_flag": "numeric",
    "fraud_label": "numeric",
    "item_count": "numeric",
    "total_quantity": "numeric",
    "unique_products": "numeric",
    "unique_merchants": "numeric",
    "max_product_risk_score": "numeric",
    "avg_product_risk_score": "numeric",
    "customer_txn_count_30d": "numeric",
    "customer_avg_amount_30d": "numeric",
    "customer_unique_devices_30d": "numeric",
    "customer_unique_countries_30d": "numeric",
    "customer_unique_merchants_30d": "numeric",
    "customer_failed_payments_7d": "numeric",
    "new_device_flag": "numeric",
    "new_country_flag": "numeric",
}


# Validation Functions

def check_required_columns(
    df: pd.DataFrame,
    report: ValidationReport,
) -> None:
    missing = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing:
        report.missing_columns = missing
        report.passed = False
        report.errors.append(f"Missing required columns: {missing}")
        logger.warning("Missing columns: %s", missing)
    else:
        logger.info("All required columns present.")


def check_data_types(
    df: pd.DataFrame,
    report: ValidationReport,
) -> None:
    for col, expected_type in EXPECTED_TYPES.items():
        if col not in df.columns:
            continue

        series = df[col]

        if expected_type == "numeric":
            if not pd.api.types.is_numeric_dtype(series):
                report.type_mismatches[col] = f"expected=numeric, actual={series.dtype}"

        elif expected_type == "string":
            if not (
                pd.api.types.is_object_dtype(series)
                or pd.api.types.is_string_dtype(series)
            ):
                report.type_mismatches[col] = f"expected=string, actual={series.dtype}"

        elif expected_type == "datetime":
            if not pd.api.types.is_datetime64_any_dtype(series):
                report.type_mismatches[col] = f"expected=datetime, actual={series.dtype}"

    if report.type_mismatches:
        report.passed = False
        report.errors.append("Data type mismatches detected.")
        logger.warning("Data type mismatches found.")
    else:
        logger.info("All data types validated.")


def check_missing_values(
    df: pd.DataFrame,
    report: ValidationReport,
    threshold: float = 0.3,
) -> None:
    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0]

    if not missing_counts.empty:
        report.missing_value_counts = missing_counts.to_dict()
        for col, count in missing_counts.items():
            ratio = count / len(df)
            if ratio > threshold:
                report.passed = False
                report.errors.append(
                    f"Column '{col}' has {ratio:.1%} missing values "
                    f"(threshold={threshold:.0%})"
                )
                logger.warning(
                    "High missing values in column=%s ratio=%.2f", col, ratio
                )
    else:
        logger.info("No missing values detected.")


def check_duplicates(
    df: pd.DataFrame,
    report: ValidationReport,
) -> None:
    duplicate_count = int(df.duplicated().sum())
    report.duplicate_row_count = duplicate_count

    if duplicate_count > 0:
        logger.warning("Duplicate rows detected: %d", duplicate_count)
    else:
        logger.info("No duplicate rows detected.")

    if "payment_id" in df.columns:
        duplicate_payment_ids = int(df.duplicated(subset=["payment_id"]).sum())
        report.duplicate_payment_id_count = duplicate_payment_ids

        if duplicate_payment_ids > 0:
            report.passed = False
            report.errors.append(
                f"Duplicate payment_id values found: {duplicate_payment_ids}"
            )
            logger.warning("Duplicate payment_id detected: %d", duplicate_payment_ids)
        else:
            logger.info("No duplicate payment_id values detected.")


def check_invalid_values(
    df: pd.DataFrame,
    report: ValidationReport,
) -> None:
    invalid_checks: Dict[str, int] = {}

    if "amount_usd_equivalent" in df.columns:
        invalid_checks["negative_amount_usd_equivalent"] = int(
            (df["amount_usd_equivalent"] < 0).sum()
        )

    if "transaction_hour" in df.columns:
        invalid_checks["invalid_transaction_hour"] = int(
            ((df["transaction_hour"] < 0) | (df["transaction_hour"] > 23)).sum()
        )

    if "ip_risk_score" in df.columns:
        invalid_checks["invalid_ip_risk_score"] = int(
            ((df["ip_risk_score"] < 0) | (df["ip_risk_score"] > 1)).sum()
        )

    if "velocity_score" in df.columns:
        invalid_checks["invalid_velocity_score"] = int(
            ((df["velocity_score"] < 0) | (df["velocity_score"] > 1)).sum()
        )

    if "amount_risk_score" in df.columns:
        invalid_checks["invalid_amount_risk_score"] = int(
            ((df["amount_risk_score"] < 0) | (df["amount_risk_score"] > 1)).sum()
        )

    if "device_risk_score" in df.columns:
        invalid_checks["invalid_device_risk_score"] = int(
            ((df["device_risk_score"] < 0) | (df["device_risk_score"] > 1)).sum()
        )

    if "payment_timestamp" in df.columns and pd.api.types.is_datetime64_any_dtype(df["payment_timestamp"]):
        invalid_checks["invalid_payment_timestamp"] = int(df["payment_timestamp"].isna().sum())

    report.invalid_value_checks = invalid_checks

    failed_checks = {k: v for k, v in invalid_checks.items() if v > 0}
    if failed_checks:
        report.passed = False
        report.errors.append(f"Invalid value checks failed: {failed_checks}")
        logger.warning("Invalid value checks failed: %s", failed_checks)
    else:
        logger.info("All invalid value checks passed.")


# Main Validator

def validate_dataset(df: pd.DataFrame) -> ValidationReport:
    logger.info("Starting dataset validation. Shape=%s", df.shape)
    report = ValidationReport()

    check_required_columns(df, report)
    check_data_types(df, report)
    check_missing_values(df, report)
    check_duplicates(df, report)
    check_invalid_values(df, report)

    if report.passed:
        logger.info("Validation PASSED.")
    else:
        logger.warning("Validation FAILED. See report for details.")

    return report


if __name__ == "__main__":
    dummy_data = {
        "payment_id": [1, 2, 2],
        "order_id": [101, 102, 102],
        "customer_id": [1001, 1002, 1002],
        "account_age_days": [200, 300, 300],
        "kyc_level": ["HIGH", "LOW", "LOW"],
        "customer_risk_segment": ["HIGH", "MEDIUM", "MEDIUM"],
        "repeated_beneficiary_flag": [0, 1, 1],
        "device_id": ["DEV_1", "DEV_2", "DEV_2"],
        "ip_risk_score": [0.2, 0.5, 1.3],
        "device_shared_flag": [0, 1, 1],
        "payment_status": ["success", "failed", "failed"],
        "payment_timestamp": pd.to_datetime(["2026-06-01", "2026-06-02", "2026-06-02"]),
        "payment_method": ["CARD", "UPI", "UPI"],
        "transaction_channel": ["WEB", "MOBILE", "MOBILE"],
        "geo_risk_level": ["LOW", "HIGH", "HIGH"],
        "transaction_direction": ["INBOUND", "OUTBOUND", "OUTBOUND"],
        "counterparty_country": ["India", "Singapore", "Singapore"],
        "instrument_age_days": [100, 50, 50],
        "transaction_hour": [10, 26, 26],
        "amount_usd_equivalent": [100.0, -50.0, -50.0],
        "velocity_score": [0.2, 0.5, 1.5],
        "amount_risk_score": [0.2, 0.3, 0.3],
        "device_risk_score": [0.2, 0.3, 0.3],
        "transaction_frequency_24h": [2, 5, 5],
        "transaction_frequency_7d": [5, 10, 10],
        "geo_mismatch_flag": [0, 1, 1],
        "sanctions_country_flag": [0, 0, 0],
        "high_risk_corridor_flag": [0, 1, 1],
        "structuring_flag": [0, 1, 1],
        "fraud_label": [0, 1, 1],
        "item_count": [1, 2, 2],
        "total_quantity": [1, 3, 3],
        "unique_products": [1, 2, 2],
        "unique_merchants": [1, 2, 2],
        "max_product_risk_score": [0.1, 0.5, 0.5],
        "avg_product_risk_score": [0.1, 0.3, 0.3],
        "customer_txn_count_30d": [5, 10, 10],
        "customer_avg_amount_30d": [80.0, 120.0, 120.0],
        "customer_unique_devices_30d": [1, 2, 2],
        "customer_unique_countries_30d": [1, 2, 2],
        "customer_unique_merchants_30d": [2, 3, 3],
        "customer_failed_payments_7d": [0, 1, 1],
        "new_device_flag": [0, 1, 1],
        "new_country_flag": [0, 1, 1],
    }

    df_test = pd.DataFrame(dummy_data)
    report = validate_dataset(df_test)
    report.summary()