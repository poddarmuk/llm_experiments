"""Main entry point for llm_experiments."""

import os
from dotenv import load_dotenv


def main() -> None:
    # Load environment variables from .env file if present
    load_dotenv()
    print("Welcome to llm-experiments!")
    print(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")


if __name__ == "__main__":
    main()
