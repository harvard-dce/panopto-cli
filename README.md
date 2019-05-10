## panopto-cli

Command-line tool for interacting with the Panopto soap api

### Install

Python 3 is required.

`pip install panopto-cli`


Once installed the `panopto` command should be available in your path. You can execute `panopto --help` to confirm it's working and see the basic, top-level command groups:

```
Usage: panopto [OPTIONS] COMMAND [ARGS]...

Options:
  --user TEXT
  --password TEXT
  --host TEXT
  --help           Show this message and exit.

Commands:
  AccessManagement
  RemoteRecorderManagement
  SessionManagement
  UsageReporting
  UserManagement
```

##### Config file

To avoid entering the user/pass/host options each time, you can create a json config file at `~/.panopto-cli` with the following format:

```json
{
    "user": "me@example.com",
    "password": "mypassword",
    "host": "something.hosted.panopto.com"
}
```

### Usage

The cli works by introspecting the SOAP API's wsdl descriptions. In theory, any service/port/binding defined by the wsdl can be executed via the cli by combining the top-level service with a subcommand (the port/binding). For example:

`panopto UsageReporting DescribeReportTypes`

Output:

```json
[
 "FolderUsage",
 "SessionUsage",
 "UserViewingUsage",
 "UserCreationUsage",
 "LastLoginTime",
 "SessionsViewsByViewingType",
 "SessionsCreatedOrEdited",
 "RemoteRecorderUsage",
 "SystemViews"
]
```

Append `--help` to the subcommand to see the available options:

`panopto UsageReporting GetFolderSummaryUsage --help`

Output:

```json
Usage: panopto UsageReporting GetFolderSummaryUsage [OPTIONS]

Options:
  --folderId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity TEXT
  --help                          Show this message and exit.
```

There are currently some limitations to the introspection. For instance, the above `--help` output won't show you the allowed values for `--granularity` (they're "Hourly", "Daily" and "Weekly", fwiw). So in some cases you'll need to refer directly to the wsdl xml. It might be possible to inlcude this kind of detail in a future release.


##### Problem commands

* `RemoteRecorderManagement ScheduleRecording` - the `--recorderSettings` option is both comlex and allows multiple and the cli can't currently handle that.
* `UsageReporting GetReport` - the response is in the form of a downloadable zip file and zeep doesn't know what to do with it``
* `SessionManagement UploadTranscript` - takes a file path as an argument and I haven't figure out how to attach files


##### Report generation example

```bash
$ panopto UsageReporting QueueReport --help
Usage: panopto UsageReporting QueueReport [OPTIONS]

Options:
  --reportType TEXT
  --startTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
  
$ panopto UsageReporting DescribeReportTypes
[
 "FolderUsage",
 "SessionUsage",
 "UserViewingUsage",
 "UserCreationUsage",
 "LastLoginTime",
 "SessionsViewsByViewingType",
 "SessionsCreatedOrEdited",
 "RemoteRecorderUsage",
 "SystemViews"
]

$ panopto UsageReporting QueueReport --reportType FolderUsage --startTime 2019-04-01 --endTime 2019-04-30
"c746717d-dcb9-4733-8e32-aa3f01307db4"

$ panopto UsageReporting GetRecentReports --help
Usage: panopto UsageReporting GetRecentReports [OPTIONS]

Options:
  --reportType TEXT
  --help             Show this message and exit.
  
$ panopto UsageReporting GetRecentReports --reportType FolderUsage
[
 {
  "EndTime": "2019-04-30T04:00:00+00:00Z",
  "IsAvailable": false,
  "ReportId": "c746717d-dcb9-4733-8e32-aa3f01307db4",
  "ReportTime": null,
  "ReportType": "FolderUsage",
  "StartTime": "2019-04-01T04:00:00+00:00Z"
 }
]

$ panopto UsageReporting GetReport --reportId c746717d-dcb9-4733-8e32-aa3f01307db4
Server returned HTTP status 204 (no content available)
```
### WSDL reference

* `https://[your host]/Panopto/PublicAPI/4.0/AccessManagement.svc?singleWsdl`
* `https://[your host]/Panopto/PublicAPI/4.2/RemoteRecorderManagement.svc?singleWsdl`
* `https://[your host]/Panopto/PublicAPI/4.6/SessionManagement.svc?singleWsdl`
* `https://[your host]/Panopto/PublicAPI/4.0/UsageReporting.svc?singleWsdl`
* `https://[your host]/Panopto/PublicAPI/4.0/UserManagement.svc?singleWsdl`

## Contributors

* Jay Luker - [lbjay](https://github.com/lbjay)
* Anshi Moreno Jimenez - [amorenojimenez1](https://github.com/amorenojimenez1)

