from BunnyCDN.CDN import CDN
from BunnyCDN.Storage import Storage
from config import Config

storage_api_key="7ac93fd8-09f9-4a9f-acc6c3515889-6e83-44d0"
storage_zone_name="stocksales"

obj_storage = Storage(storage_api_key,storage_zone_name)
obj_cdn = CDN("cdfca33f-7b42-4cd9-970a-d9125ad09fde")
