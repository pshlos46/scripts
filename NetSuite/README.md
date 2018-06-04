# Export NetSuite SavedSearch as .csv

## Usage

Using `Python 3.6` run the `SavedSearchGET.py` passing as 1st and only argument the Saved Search ID you want to run, like this:

`python3.6 SavedSearchGET.py 42`

as a result in the same folder that you'll execute the script you'll see:

`SavedSearch42.csv` 

which will contain the results of the Saved Search in .csv format.

10MB is the only documented limit from NetSuite.

## Installation

`RESTletSavedSearch.js` has to be uploaded in NetSuite as RESTlet and the `GET` action should be mapped to `executeSavedSearch` function. 

Then run `SavedSearchGET.py` using your NLauth authentication, preferably by using ENV variables.



# Import to NetSuite from Online .csv

Use `csvImportNS.js` to import straight results from an online .csv (like from heroku dataclips, redash, periodically updated .csv in S3 etc.) using a NetSuite mapping to Netsuite. 
You'll have to set it up as scheduled script and provide the internalID of the mapping. 

