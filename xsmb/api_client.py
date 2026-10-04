import logging
import requests
from xsmb.config import api_url, api_key, setup_logging



def fetch_all_pages(pages: int, limit: int, api_key: str, api_url: str) -> list[dict]:
    all_draws = []
    for page in range(1, pages + 1):
        headers = {
            "X-API-Key": api_key,
            "Accept": "application/json",
        }

        query_params = {
            "limit": limit,
            "page": page,
        }

        try:
            response = requests.get(
                api_url,
                headers=headers,
                params=query_params
            )

            response.raise_for_status()
            data = response.json()

            page_data = data["data"]
            all_draws.extend(page_data)

            logging.info("Page %d - Lấy được %d bản ghi", page, len(page_data))
        except requests.exceptions.HTTPError as http_err:
            print(f"Page {page} - HTTP error: {http_err}")
            break

        except Exception as err:
            print(f"Page {page} - Other error: {err}")
            break
    return all_draws

if __name__ == "__main__":
    setup_logging("INFO")
    pages = 5
    limit = 100
    logging.info("Bắt đầu lấy %d trang (limit=%d)...", pages, limit)
    all_draws = fetch_all_pages(pages, limit, api_key, api_url)
    logging.info("Tổng cộng lấy được %d bản ghi", len(all_draws))
