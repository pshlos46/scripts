function updater() // updates the sheet, based on a trigger
{
  SpreadsheetApp.openById('').getRange('').setValue('=IMPORTRANGE("","A:Z")')
}


function Copy() // Copies a snapshot of a sheet in a new sheet
{
 var aaa = SpreadsheetApp.openById('');    			//source ID
 var aa = aaa.getSheetByName('');		   			//replace with source Sheet tab name
 var range = aa.getRange('A:Z');  		   			//assign the range you want to copy
 var data = range.getValues();
 var name = (new Date()).toLocaleDateString();		// set date to type March 1, 2018, May 1, 2018 etc.
 SpreadsheetApp.openById('').insertSheet(name);
 var naa = SpreadsheetApp.openById('');    			//replace with destination ID
 var ns = naa.getSheetByName(name);                 //replace with destination Sheet tab name
 var bs = ns.getRange('A:Z');
 bs.setValues(data);
}


// Function to create XLS and send email

function downloadXLS() {
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const d = new Date();
  
  var fileId = '';
  var file = Drive.Files.get(fileId);
  var folderId = ''; 
  var url = file.exportLinks[MimeType.MICROSOFT_EXCEL];

  var options = {
    headers: {
      Authorization:"Bearer "+ScriptApp.getOAuthToken()
    },
    muteHttpExceptions : true        /// Get failure results
  }

  var response = UrlFetchApp.fetch(url, options);
  var status = response.getResponseCode();
  var result = response.getContentText();
  if (status != 200) {
    // Get additional error message info, depending on format
    if (result.toUpperCase().indexOf("<HTML") !== -1) {
      var message = strip_tags(result);
    }
    else if (result.indexOf('errors') != -1) {
      message = JSON.parse(result).error.message;
    }
    throw new Error('Error (' + status + ") " + message );
  }
  
  var doc = response.getBlob();
  var date = (new Date()).toLocaleDateString();
  var time = (new Date()).toLocaleTimeString();
  var attach = [DriveApp.getFolderById(folderId).createFile(doc).setName(date+'TPS-Reports')]
  var email = "office@space.com"
  var subject = "TPS reports" +monthNames[d.getMonth()]+d.getFullYear();
  var body = "Please see attached what you need";
  MailApp.sendEmail(email,subject ,body, {name: 'Mail sender especial', attachments:attach});
}
