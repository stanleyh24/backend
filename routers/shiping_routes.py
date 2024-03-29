from fastapi import APIRouter, Depends, status
from .schemas import ShipTo
import httpx
from utils.utils import get_weight

shiping = APIRouter(
    prefix='/shiping',
    tags=['shiping']
)

@shiping.post('/')
async def get_shipings(request:ShipTo):
    requestData = {
  "RateRequest": {
    "Request": {
      "SubVersion": "1703",
      "TransactionReference": {
        "CustomerContext": " "
      }
    },
    "Shipment": {
      "ShipmentRatingOptions": {
        "UserLevelDiscountIndicator": "TRUE"
      },
      "Shipper": {
        "Name": "Boutique Caoba",
        "ShipperNumber": " ",
        "Address": {
          "AddressLine": "CALLE EL CONDE NO.109 ZONA COLONIAL",
          "City": "SANTO DOMINGO",
          "StateProvinceCode": "DO",
          "PostalCode": "10210",
          "CountryCode": "DO"
        }
      },
      "ShipTo": {
        "Name": request.Name,
        "Address": {
          "AddressLine": request.AddressLine,
          "City": request.City,
          "PostalCode": request.PostalCode,
          "CountryCode": request.CountryCode,
        }
      },
      "ShipFrom": {
        "Name": "Boutique Caoba",
        "Address": {
          "AddressLine": "CALLE EL CONDE NO.109 ZONA COLONIAL",
          "City": "SANTO DOMINGO",
          "StateProvinceCode": "DO",
          "PostalCode": "10210",
          "CountryCode": "DO"
        }
      },
      "ShipmentTotalWeight": {
        "UnitOfMeasurement": {
          "Code": "LBS",
          "Description": "Pounds"
        },
        "Weight": str(int(request.Weight))
      },
      "Package": {
        "PackagingType": {
          "Code": "02",
          "Description": "Package"
        },
        "Dimensions": {
          "UnitOfMeasurement": {
            "Code": "IN"
          },
          "Length": str(int(request.Packaging_length)),
          "Width": str(int(request.Packaging_width)),
          "Height": str(int(request.Packaging_height))
        },
        "PackageWeight": {
          "UnitOfMeasurement": {
            "Code": "LBS"
          },
          "Weight": get_weight(request.Weight)
        }
      }
    }
  }
}
    r = httpx.post('https://wwwcie.ups.com/ship/v1/rating/Shop', headers={
    "Content-Type": "application/json",
    "AccessLicenseNumber": "FDCDA7F0602CCF72",
    "Username": "boutiquecaoba",
    "Password": "Greetings.01",
    "transactionSrc": "boutiquecaoba",
    "transId":"Tran123"
}, json=requestData)
    body=r.json()
    return body