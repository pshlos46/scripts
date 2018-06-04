/*
Use the below as a Scheduled SuiteScript to import straight results from an online .csv
(like from heroku dataclips, redash, periodically updated .csv in S3 etc.)
using a NetSuite mapping to Netsuite
*/

function scheduled()
{
	nlapiLogExecution('AUDIT', 'Import from csv started...')

    // Set below the file you'll use for imports in the file cabinet 
    var file = 'admin-netsuite/import.csv';


	var mappingFileId = ""; //use internal id of Saved CSV Import mapping
	var primaryFile = nlapiLoadFile(file); //using the internal id of the file stored in the File Cabinet
	var job = nlapiCreateCSVImport();
	job.setMapping(mappingFileId);
	job.setPrimaryFile(primaryFile);
	job.setOption("jobName", "job2Import");

	//returns the internal id of the new job created in workqueue for logging
	var jobId = nlapiSubmitCSVImport(job);
    nlapiLogExecution('AUDIT', 'Import from csv finished. job id:');
	nlapiLogExecution('AUDIT', jobId)

}