from aepp.connector import AdobeRequest
import os
import json

def get_aepp_connection(sandbox: str):
    """
    Initialize and return an AEPP connection for the given sandbox.
    Credentials are loaded from 'aepp_config.json' or environment variables.
    """
    config_path = os.path.join(os.path.dirname(__file__), '..', 'aepp_config.json')
    credentials = {}

    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            all_configs = json.load(f)
            credentials = all_configs.get(sandbox, {})
    else:
        # Fallback to environment variables
        credentials = {
            "client_id": os.getenv("AEPP_CLIENT_ID"),
            "client_secret": os.getenv("AEPP_CLIENT_SECRET"),
            "technical_account_id": os.getenv("AEPP_TECHNICAL_ACCOUNT_ID"),
            "org_id": os.getenv("AEPP_ORG_ID"),
            "private_key_path": os.getenv("AEPP_PRIVATE_KEY_PATH"),
            "meta_scopes": os.getenv("AEPP_META_SCOPES", "").split(","),
            "sandbox": sandbox
        }

    if not credentials:
        raise ValueError(f"No credentials found for sandbox '{sandbox}'")

    return AdobeRequest(
        client_id=credentials.get("client_id"),
        client_secret=credentials.get("client_secret"),
        technical_account_id=credentials.get("technical_account_id"),
        org_id=credentials.get("org_id"),
        private_key_path=credentials.get("private_key_path"),
        meta_scopes=credentials.get("meta_scopes"),
        sandbox=credentials.get("sandbox")
    )