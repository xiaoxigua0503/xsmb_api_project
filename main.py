import argparse
import logging

from xsmb.api_client import fetch_all_pages
from xsmb.config import api_url,api_key,setup_logging
from xsmb.storage import save_json, export_csv
from xsmb.transform import filter_region, to_dataframe


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lấy kết quả xổ số Miền Bắc (XSMB)")
    parser.add_argument("--pages", type=int, default=5, help="Số trang cần lấy (mặc định: 5)")
    parser.add_argument("--limit", type=int, default=100, help="Số bản ghi mỗi trang (mặc định: 100)")
    parser.add_argument("--output-json", default="full_draws.json", help="File JSON đầu ra")
    parser.add_argument("--output-csv", default="xsmb_results.csv", help="File CSV đầu ra")
    parser.add_argument(
        "--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"]
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logger = logging.getLogger(__name__)
    setup_logging(args.log_level)

    logger.info("Bắt đầu lấy %d trang (limit=%d)...", args.pages, args.limit)
    all_draws = fetch_all_pages(pages=args.pages, limit=args.limit, api_key=api_key, api_url=api_url)
    logger.info("Tổng cộng lấy được %d bản ghi", len(all_draws))

    save_json(all_draws, args.output_json)
    logger.info("Đã lưu dữ liệu thô vào %s", args.output_json)

    mien_bac_draws = filter_region(all_draws)
    df = to_dataframe(mien_bac_draws)
    export_csv(df, args.output_csv)
    logger.info("Đã lưu %d dòng kết quả Miền Bắc vào %s", len(df), args.output_csv)


if __name__ == "__main__":
    main()
