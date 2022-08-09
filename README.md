#Project
Stock Investing Project has the purpose of identifying great US companies for investing in the long run. 

#APIs
## Helpful video and repository
https://www.youtube.com/watch?v=-RSowRQ9CRU
https://github.com/Peter-Staadecker/Edgar-and-the-Python

## SEC api documentation
https://www.sec.gov/edgar/sec-api-documentation

### Getting CIK, Ticker & Name
"fields":["cik","name","ticker","exchange"]
https://www.sec.gov/files/company_tickers_exchange.json

### Example getting EarningsPerShareDiluted from companyconcept url
Note: The CIK in the url has to follow the format CIK and 10 numbers. Example: CIK0001318605
"https://data.sec.gov/api/xbrl/companyconcept/CIK" + cikStr + "/us-gaap/EarningsPerShareDiluted.json"

## Financial Modeling Prep API documentation (stockFundamentals)
https://site.financialmodelingprep.com/developer/docs/