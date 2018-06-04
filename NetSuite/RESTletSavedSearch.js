/* 
This is deployed to netsuite as RESTlet and you hit the link provided by netsuite to achieve functionality.
Configure in NetSuite GET action to executeSavedSearch function
*/

function executeSavedSearch(options) {
  if ( !options.searchId ) {
    return { error: 'Must provide the searchId of the saved search', options: options };
  }

  var SLICE_LIMIT = 1000;
  var search = nlapiLoadSearch(null, options.searchId);
  var resultset = search.runSearch();

  var results = [];

  var index = 0;
  do {
    var subset = resultset.getResults(index, index+1000);
    if ( !subset ) break;
    subset.forEach( function (row) {
      results.push(row);
      index++;
    });
  } while (subset.length === SLICE_LIMIT);

  return results;
}
