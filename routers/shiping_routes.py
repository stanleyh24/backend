from fastapi import APIRouter, Depends, status
import httpx

shiping = APIRouter(
    prefix='/shiping',
    tags=['shiping']
)

@shiping.get('/')
async def get_shipings():
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
        "Name": "Sarita Lynn",
        "Address": {
          "AddressLine": "355 West San Fernando Street",
          "City": "San Jose",
          "StateProvinceCode": "CA",
          "PostalCode": "95113",
          "CountryCode": "US"
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
        "Weight": "2"
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
          "Length": "10",
          "Width": "7",
          "Height": "5"
        },
        "PackageWeight": {
          "UnitOfMeasurement": {
            "Code": "LBS"
          },
          "Weight": "2"
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