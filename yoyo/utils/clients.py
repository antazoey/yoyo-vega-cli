from enum import Enum
from typing import Dict

import vegaapiclient as vac


class GRPCRegion(Enum):
    NETHERLANDS = "n06.testnet.vega.xyz"
    FINLAND = "n07.testnet.vega.xyz"
    HONG_KONG = "n08.testnet.vega.xyz"
    USA = "n09.testnet.vega.xyz"
    JAPAN = "n10.testnet.vega.xyz"


class VegaRestClient:
    def __init__(self, node_url_grpc: str):
        self._client = vac.VegaCoreDataClient(node_url_grpc)

    @classmethod
    def from_region(cls, region: GRPCRegion):
        return cls(region.value)

    def get_parties(self) -> Dict:
        req = vac.data_node.api.v1.trading_data.PartiesRequest()
        response = self._client.Parties(req)
        return response.json()
