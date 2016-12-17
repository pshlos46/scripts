/*
 save tabs is a java script for Acrobat Reader
 on Linux put it usually in ~/.adobe/Acrobat/9.0/JavaScripts
 on Windows and Adobe DC -> C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Javascripts
 and in Acrobat Menu (Edit>Preferences>Javascript) ENABLE "Enable menu items JavaScript execution privileges"
*/
var delim= '|';
var parentMenu="View";

/*
 Loading Saved Tabs
*/
function LoadTabs()
{    

    if( global.tabs_opened == null )
    {
        return;
    }

    var flat= global.tabs_opened.split( delim );
    for( i= 0; i< flat.length; i+=2)
    {
        try
        {
            app.openDoc( flat[i] );
            app.execMenuItem( "FirstPage" );
            for( ii= 0; ii< flat[i+1]; ++ii )
            {
                app.execMenuItem( "NextPage" );
            }
        }
        catch( ee )
        {
            app.alert("Error while opening the requested document.\n"+flat[i],3);
        }
    }
}

/*
 Function with trusted section returning opened documents
*/
trustedActiveDocs = app.trustedFunction ( function()
{
    app.beginPriv();
    var d = app.activeDocs;
    app.endPriv();
    return d;
})

/*
 Saving Tabs that are opened
*/
function SaveTabs()
{
    var d = trustedActiveDocs();
    var tabs = '';

    for ( var i=0;i<d.length; i++)
    {
        if(i>0)
            tabs+=delim;
            //app.alert(d[i].path+"------"+d[i].pageNum,3);
        tabs+= d[i].path;
        tabs+= delim;
        tabs+= d[i].pageNum;
    }
    global.tabs_opened = tabs;
    global.setPersistent( "tabs_opened", true );
    app.alert("Tabs Saved",3);

}
/*
 Toggle auto load tabs
 automatically loading tabs when reader starts
*/
function ToggleAuto()
{
    if(global.tabs_auto == 0 || global.tabs_auto == null)
    {
        global.tabs_auto=1;
        global.setPersistent( "tabs_auto", true );
        app.alert("Tabs auto loading enabled",3);
    }
    else
    {
        global.tabs_auto=0;
        global.setPersistent( "tabs_auto", true );
        app.alert("Tabs auto loading disabled",3);
    }
}

app.addMenuItem( {
                    cName: "-",
                    cParent: parentMenu,
                    cExec: "void(0);" } );

app.addMenuItem( {
                    cName: "&Save Tabs",
                    cParent: parentMenu,
                    cExec: "SaveTabs();"
                } );

app.addMenuItem( {
                    cName: "&Load Tabs",
                    cParent: parentMenu,
                    cExec: "LoadTabs();"
                } );

app.addMenuItem( {
                    cName: "Toggle auto load",
                    cParent: parentMenu,
                    cExec: "ToggleAuto();"
                } );
	
if(global.tabs_auto==1)
{
    LoadTabs();
}
