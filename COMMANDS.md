## AccessManagement

### GetUserAccessDetails

```
Usage: panopto AccessManagement GetUserAccessDetails [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.
```

### GetSelfUserAccessDetails

```
Usage: panopto AccessManagement GetSelfUserAccessDetails [OPTIONS]

Options:
  --help  Show this message and exit.
```

### GetSessionAccessDetails

```
Usage: panopto AccessManagement GetSessionAccessDetails [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.
  ```
 
### GetFolderAccessDetails
  
```
Usage: panopto AccessManagement GetFolderAccessDetails [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.
```

### GetGroupAccessDetails

```
Usage: panopto AccessManagement GetGroupAccessDetails [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.
```

### GrantUsersAccessToFolder

```
Usage: panopto AccessManagement GrantUsersAccessToFolder [OPTIONS]

Options:
  --folderId TEXT
  --userIds TEXT
  --role TEXT
  --help           Show this message and exit.
```

### GrantUsersViewersAccessToSession

```
Usage: panopto AccessManagement GrantUsersViewerAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userIds TEXT
  --help            Show this message and exit.
  ```
  
### GrantGroupAccessToFolder

```
Usage: panopto AccessManagement GrantGroupAccessToFolder [OPTIONS]

Options:
  --folderId TEXT
  --groupId TEXT
  --role TEXT
  --help           Show this message and exit.
```

### GrantGroupViewerAccessToSession

```
Usage: panopto AccessManagement GrantGroupViewerAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --groupId TEXT
  --help            Show this message and exit.
```

### GrantAllAuthenticatedUsersGroupAccessToFolder

```
Usage: panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --role TEXT
  --help           Show this message and exit.
```

### GrantAllAuthenticatedUsersGroupsAccessToSession

```
sage: panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --role TEXT
  --help            Show this message and exit.
```

### GrantPublicGroupAccessToFolder

```
Usage: panopto AccessManagement GrantPublicGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --role TEXT
  --help           Show this message and exit.
  ```
  
  ### GrantPublicGroupAccessToSession
  
  ```
  Usage: panopto AccessManagement GrantPublicGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --role TEXT
  --help            Show this message and exit.
  ```
  
 ### RevokeAllImplicitGroupAccessToFolder
 
 ```
 Usage: panopto AccessManagement RevokeAllImplicitGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.
  ```
  
  ### RevokeAllImplicitGroupAccessToSession
  
  ```
  Usage: panopto AccessManagement RevokeAllImplicitGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.
  ```
  
  ### UpdateFolderIsPublic
  
  ```
  Usage: panopto AccessManagement UpdateFolderIsPublic [OPTIONS]

Options:
  --folderId TEXT
  --isPublic TEXT
  --help           Show this message and exit.
  ```
  
  ### UpdateSessionIsPublic
  
  ```
  Usage: panopto AccessManagement UpdateSessionIsPublic [OPTIONS]

Options:
  --sessionId TEXT
  --isPublic TEXT
  --help            Show this message and exit.
  ```
  
  ### UpdateSessionInheritViewerAccess
  
  ```
  Usage: panopto AccessManagement UpdateSessionInheritViewerAccess 
           [OPTIONS]

Options:
  --sessionId TEXT
  --inheritViewerAccess TEXT
  --help                      Show this message and exit.
 ```
 
 ### RevokeUsersAccessFromFolder
 
 ```
 Usage: panopto AccessManagement RevokeUsersAccessFromFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --userIds TEXT
  --role TEXT
  --help           Show this message and exit.
  ```
  
### RevokeUsersViewerAccessFromSession

```
Usage: panopto AccessManagement RevokeUsersViewerAccessFromSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userIds TEXT
  --help            Show this message and exit.
```

### RevokeGroupAccessFromFolder

```
Usage: panopto AccessManagement RevokeGroupAccessFromFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --groupId TEXT
  --role TEXT
  --help           Show this message and exit.
```

### RevokeGroupViewerAccessFromSession

```
Usage: panopto AccessManagement RevokeGroupViewerAccessFromSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --groupId TEXT
  --help            Show this message and exit.
```

## RemoteRecorderManagement 

### GetRemoteRecordersById

```
Usage: panopto RemoteRecorderManagement GetRemoteRecordersById 
           [OPTIONS]

Options:
  --remoteRecorderIds TEXT
  --help                    Show this message and exit.
```

### GetRemoteRecordersByExternalId

```
Usage: panopto RemoteRecorderManagement GetRemoteRecordersByExternalId 
           [OPTIONS]

Options:
  --externalIds TEXT
  --help              Show this message and exit.
```

### UpdateRemoteRecorderExternalId

```
Usage: panopto RemoteRecorderManagement UpdateRemoteRecorderExternalId 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --externalId TEXT
  --help                   Show this message and exit.
```

### ListRecorders

```
Usage: panopto RemoteRecorderManagement ListRecorders [OPTIONS]

Options:
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --sortBy TEXT
  --help                      Show this message and exit.
  ```
  
  ### ScheduleRecording
  
  ```
  Usage: panopto RemoteRecorderManagement ScheduleRecording [OPTIONS]

Options:
  --name TEXT
  --folderId TEXT
  --isBroadcast TEXT
  --start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --recorderSettings TEXT
  --help                          Show this message and exit.
  ```
  
  ### ScheduleRecurringRecording
  
  ```
  Usage: panopto RemoteRecorderManagement ScheduleRecurringRecording 
           [OPTIONS]

Options:
  --scheduledSessionId TEXT
  --daysOfWeek TEXT
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
  ```
  
  ### UpdateRecordingTime
  
  ```
  Usage: panopto RemoteRecorderManagement UpdateRecordingTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
  ```
  
  ### UpdateRecordingSettings
  
  ```
  Usage: panopto RemoteRecorderManagement UpdateRecordingSettings 
           [OPTIONS]

Options:
  --sessionId TEXT
  --recorderSettings TEXT
  --help                   Show this message and exit.
  ```
  
  ### GetDefaultFolderForRecorder
  
  ```
  Usage: panopto RemoteRecorderManagement GetDefaultFolderForRecorder 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --help                   Show this message and exit.
```

### GetMachineSidForRecorder

```
Usage: panopto RemoteRecorderManagement GetMachineSidForRecorder 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --help                   Show this message and exit.
```

## SessionManagement

### GetFolder

```
Usage: panopto SessionManagement AddFolder [OPTIONS]

Options:
  --name TEXT
  --parentFolder TEXT
  --isPublic TEXT
  --help               Show this message and exit.
```

### GetSession

```
Usage: panopto SessionManagement AddSession [OPTIONS]

Options:
  --name TEXT
  --folderId TEXT
  --isBroadcast TEXT
  --help              Show this message and exit.
```

### GetFoldersById

```
Usage: panopto SessionManagement GetFoldersById [OPTIONS]

Options:
  --folderIds TEXT
  --help            Show this message and exit.
```

### GetFoldersWithExternalContextById

```
Usage: panopto SessionManagement GetFoldersWithExternalContextById 
           [OPTIONS]

Options:
  --folderIds TEXT
  --help            Show this message and exit.
```

### GetFoldersByExternalId

```
Usage: panopto SessionManagement GetFoldersByExternalId [OPTIONS]

Options:
  --folderExternalIds TEXT
  --help                    Show this message and exit.
```

### GetFoldersWithExternalContextByExternalId

```
Usage: panopto SessionManagement GetFoldersWithExternalContextByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT
  --help                    Show this message and exit.
```

### GetAllFoldersByExternalId

```
Usage: panopto SessionManagement GetAllFoldersByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT
  --providerNames TEXT
  --help                    Show this message and exit.
```

### GetAllFoldersWithExternalContextByExternalId

```
Usage: panopto SessionManagement GetAllFoldersWithExternalContextByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT
  --providerNames TEXT
  --help                    Show this message and exit.
```

### GetSessionsById

```
Usage: panopto SessionManagement GetSessionsById [OPTIONS]

Options:
  --sessionIds TEXT
  --help             Show this message and exit.
```

### GetSessionsByExternalId

```
Usage: panopto SessionManagement GetSessionsByExternalId [OPTIONS]

Options:
  --sessionExternalIds TEXT
  --help                     Show this message and exit.
```

### GetSessionsList

```
Usage: panopto SessionManagement GetSessionsList [OPTIONS]

Options:
  --request TEXT
  --searchQuery TEXT
  --help              Show this message and exit.
```

### GetFoldersList

```
Usage: panopto SessionManagement GetFoldersList [OPTIONS]

Options:
  --request TEXT
  --searchQuery TEXT
  --help              Show this message and exit.
```

### GetFoldersWithExternalContextList

```
Usage: panopto SessionManagement GetFoldersWithExternalContextList 
           [OPTIONS]

Options:
  --request TEXT
  --searchQuery TEXT
  --help              Show this message and exit.
```

### GetCreatorFoldersList

```
Usage: panopto SessionManagement GetCreatorFoldersList [OPTIONS]

Options:
  --request TEXT
  --searchQuery TEXT
  --help              Show this message and exit.
```

### GetCreatorFoldersWithExternalContextList

```
Usage: panopto SessionManagement GetCreatorFoldersWithExternalContextList 
           [OPTIONS]

Options:
  --request TEXT
  --searchQuery TEXT
  --help              Show this message and exit.
```

### UpdateSessionName

```
Usage: panopto SessionManagement UpdateSessionName [OPTIONS]

Options:
  --sessionId TEXT
  --name TEXT
  --help            Show this message and exit.
```

### UpdateSessionDescription

```
Usage: panopto SessionManagement UpdateSessionDescription [OPTIONS]

Options:
  --sessionId TEXT
  --description TEXT
  --help              Show this message and exit.
```

### UpdateSessionIsBroadcast

```
Usage: panopto SessionManagement UpdateSessionIsBroadcast [OPTIONS]

Options:
  --sessionId TEXT
  --isBroadcast TEXT
  --help              Show this message and exit.
```

### UpdateSessionSetPanoptoBroadcast

```
Usage: panopto SessionManagement UpdateSessionSetPanoptoBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.
```

### UpdateSessionSetRTMPBroadcast

```
Usage: panopto SessionManagement UpdateSessionSetRTMPBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.
```

### UpdateSessionCreateRTMPStreams

```
Usage: panopto SessionManagement UpdateSessionCreateRTMPStreams 
           [OPTIONS]

Options:
  --sessionId TEXT
  --countToAdd TEXT
  --arePrimaries TEXT
  --help               Show this message and exit.
```

### UpdateSessionUpdateRTMPStreamTypes

```
Usage: panopto SessionManagement UpdateSessionUpdateRTMPStreamTypes 
           [OPTIONS]

Options:
  --sessionId TEXT
  --streamKeys TEXT
  --setAsPrimaries TEXT
  --help                 Show this message and exit.
```

### UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand

```
Usage: panopto SessionManagement UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand 
           [OPTIONS]

Options:
  --sessionId TEXT
  --streamKeys TEXT
  --enabled TEXT
  --help             Show this message and exit.
```

### UpdateSessionOwner

```
Usage: panopto SessionManagement UpdateSessionOwner [OPTIONS]

Options:
  --sessionIds TEXT
  --newOwnerUserKey TEXT
  --help                  Show this message and exit.
```

### MoveSessions

```
Usage: panopto SessionManagement MoveSessions [OPTIONS]

Options:
  --sessionIds TEXT
  --folderId TEXT
  --help             Show this message and exit.
```

### UpdateSessionExternalId

```
Usage: panopto SessionManagement UpdateSessionExternalId [OPTIONS]

Options:
  --sessionId TEXT
  --externalId TEXT
  --help             Show this message and exit.
```

### UpdateFolderName

```
Usage: panopto SessionManagement UpdateFolderName [OPTIONS]

Options:
  --folderId TEXT
  --name TEXT
  --help           Show this message and exit.
```

### UpdateFolderDescription

```
Usage: panopto SessionManagement UpdateFolderDescription [OPTIONS]

Options:
  --folderId TEXT
  --description TEXT
  --help              Show this message and exit.
```

### UpdateFolderEnablePodcast

```
Usage: panopto SessionManagement UpdateFolderEnablePodcast 
           [OPTIONS]

Options:
  --folderId TEXT
  --enablePodcast TEXT
  --help                Show this message and exit.
```

### UpdateFolderAllowPublicNotes

```
Usage: panopto SessionManagement UpdateFolderAllowPublicNotes 
           [OPTIONS]

Options:
  --folderId TEXT
  --allowPublicNotes TEXT
  --help                   Show this message and exit.
```

### UpdateFolderAllowSessionDownload

```
Usage: panopto SessionManagement UpdateFolderAllowSessionDownload 
           [OPTIONS]

Options:
  --folderId TEXT
  --allowSessionDownload TEXT
  --help                       Show this message and exit.
```

### UpdateFolderParent

```
Usage: panopto SessionManagement UpdateFolderParent [OPTIONS]

Options:
  --folderId TEXT
  --parentId TEXT
  --help           Show this message and exit.
```

### UpdateFolderExternalId

```
Usage: panopto SessionManagement UpdateFolderExternalId [OPTIONS]

Options:
  --folderId TEXT
  --externalId TEXT
  --help             Show this message and exit.
```

### UpdateFolderExternalIdWithProvider

```
Usage: panopto SessionManagement UpdateFolderExternalIdWithProvider 
           [OPTIONS]

Options:
  --folderId TEXT
  --externalId TEXT
  --SiteMembershipProviderName TEXT
  --help                          Show this message and exit.
 ```
 
 ### DeleteSessions
 
 ```
 Usage: panopto SessionManagement DeleteSessions [OPTIONS]

Options:
  --sessionIds TEXT
  --help             Show this message and exit.
```

### DeleteFolders

```
Usage: panopto SessionManagement DeleteFolders [OPTIONS]

Options:
  --folderIds TEXT
  --help            Show this message and exit.
```

### ProvisionExternalCourse

```
Usage: panopto SessionManagement ProvisionExternalCourse [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --help             Show this message and exit.
```

### EnsureExternalHierarchyBranch

```
Usage: panopto SessionManagement EnsureExternalHierarchyBranch 
           [OPTIONS]

Options:
  --externalHierarchyBranch TEXT
  --help                          Show this message and exit.
```

### ProvisionExternalCourseWithRoles

```
Usage: panopto SessionManagement ProvisionExternalCourseWithRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --roles TEXT
  --help             Show this message and exit.
```

### SetExternalCourseAccess

```
Usage: panopto SessionManagement SetExternalCourseAccess [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT
  --help             Show this message and exit.
  ```
  
  ### SetExternalCourseAccessForRoles
  
  ```
  Usage: panopto SessionManagement SetExternalCourseAccessForRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT
  --roles TEXT
  --help             Show this message and exit.
 ```
 
 ### SetCopiedExternalCourseAccess
 
 ```
 Usage: panopto SessionManagement SetCopiedExternalCourseAccess 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT
  --help             Show this message and exit.
```

### SetCopiedExternalCourseAccessForRoles

```
Usage: panopto SessionManagement SetCopiedExternalCourseAccessForRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT
  --roles TEXT
  --help             Show this message and exit.
```

### GetRecorderDownloadUrls

```
Usage: panopto SessionManagement GetRecorderDownloadUrls [OPTIONS]

Options:
  --help  Show this message and exit.
```

### CreateNoteByRelativeTime

```
Usage: panopto SessionManagement CreateNoteByRelativeTime [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --channel TEXT
  --timestamp TEXT
  --help            Show this message and exit.
 ```
 
 ### CreateNoteByAbsoluteTime
 
 ```
 Usage: panopto SessionManagement CreateNoteByAbsoluteTime [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --channel TEXT
  --timestamp [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### EditNote

```
Usage: panopto SessionManagement EditNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --newText TEXT
  --help            Show this message and exit.
  ```
  
### DeleteNote

```
Usage: panopto SessionManagement DeleteNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --help            Show this message and exit.
```

### GetNote

```
Usage: panopto SessionManagement GetNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --help            Show this message and exit.
```

### ListNotes

```
Usage: panopto SessionManagement ListNotes [OPTIONS]

Options:
  --sessionId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --creatorId TEXT
  --channel TEXT
  --searchQuery TEXT
  --help                      Show this message and exit.
 ```
 
 ### AreUsersNotesPublic
 
 ```
 Usage: panopto SessionManagement AreUsersNotesPublic [OPTIONS]

Options:
  --userId TEXT
  --sessionId TEXT
  --help            Show this message and exit.
```

### SetNotesPublic

```
Usage: panopto SessionManagement SetNotesPublic [OPTIONS]

Options:
  --sessionId TEXT
  --areNotesPublic TEXT
  --help                 Show this message and exit.
```

### IsDropbox

```
Usage: panopto SessionManagement IsDropbox [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.
```

### CreateCaptionByRelativeTime

```
Usage: panopto SessionManagement CreateCaptionByRelativeTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --timestamp TEXT
  --help            Show this message and exit.
```

### CreateCaptionByAbsoluteTime

```
Usage: panopto SessionManagement CreateCaptionByAbsoluteTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --timestamp [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### UploadTranscript

```
Usage: panopto SessionManagement UploadTranscript [OPTIONS]

Options:
  --sessionId TEXT
  --file TEXT
  --help            Show this message and exit.
```

### GetFoldersAvailabilitySettings

```
Usage: panopto SessionManagement GetFoldersAvailabilitySettings 
           [OPTIONS]

Options:
  --folderIds TEXT
  --help            Show this message and exit.
```

### GetSessionsAvailabilitySettings

```
Usage: panopto SessionManagement GetSessionsAvailabilitySettings 
           [OPTIONS]

Options:
  --sessionIds TEXT
  --help             Show this message and exit.
```

### UpdateFoldersAvailabilityStartSettings

```
Usage: panopto SessionManagement UpdateFoldersAvailabilityStartSettings 
           [OPTIONS]

Options:
  --folderIds TEXT
  --settingType TEXT
  --startDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --overrideSessionsSettings TEXT
  --help                          Show this message and exit.
```

### UpdateFoldersAvailabilityEndSettings

```
Usage: panopto SessionManagement UpdateFoldersAvailabilityEndSettings 
           [OPTIONS]

Options:
  --folderIds TEXT
  --settingType TEXT
  --endDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --overrideSessionsSettings TEXT
  --help                          Show this message and exit.
```

### UpdateSessionsAvailabilityStartSettings

```
Usage: panopto SessionManagement UpdateSessionsAvailabilityStartSettings 
           [OPTIONS]

Options:
  --sessionIds TEXT
  --settingType TEXT
  --startDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### UpdateSessionsAvailabilityEndSettings

```
Usage: panopto SessionManagement UpdateSessionsAvailabilityEndSettings 
           [OPTIONS]

Options:
  --sessionIds TEXT
  --settingType TEXT
  --endDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
 ```
 
 ### GetPersonalFolderForUser
 
 ```
 Usage: panopto SessionManagement GetPersonalFolderForUser [OPTIONS]

Options:
  --userId TEXT
  --allowCreation TEXT
  --help                Show this message and exit.
```

### GetVideoDownloadURL

```
Usage: panopto SessionManagement GetVideoDownloadURL [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.
```

### UnprovisionExternalCourse

```
Usage: panopto SessionManagement UnprovisionExternalCourse 
           [OPTIONS]

Options:
  --externalContextId TEXT
  --help                    Show this message and exit.
```

## UsageReporting

### GetSystemSummaryUsage

```
Usage: panopto UsageReporting GetSystemSummaryUsage [OPTIONS]

Options:
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity TEXT
  --help                          Show this message and exit.
```

### GetFolderSummaryUsage

```
Usage: panopto UsageReporting GetFolderSummaryUsage [OPTIONS]

Options:
  --folderId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity TEXT
  --help                          Show this message and exit.
 ```
 
 ### GetSessionSummaryUsage
 
 ```
 Usage: panopto UsageReporting GetSessionSummaryUsage [OPTIONS]

Options:
  --sessionId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity TEXT
  --help                          Show this message and exit.
```

### GetSessionDetailedUsage

```
Usage: panopto UsageReporting GetSessionDetailedUsage [OPTIONS]

Options:
  --sessionId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### GetSessionExtendedDetailedUsage

```
           [OPTIONS]

Options:
  --sessionId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### GetUserDetailedUsage

```
Usage: panopto UsageReporting GetUserDetailedUsage [OPTIONS]

Options:
  --userId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --help                      Show this message and exit.
```

### GetUserExtendedDetailedUsage

```
Usage: panopto UsageReporting GetUserExtendedDetailedUsage 
           [OPTIONS]

Options:
  --userId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### GetSessionUserDetailedUsage

```
Usage: panopto UsageReporting GetSessionUserDetailedUsage [OPTIONS]

Options:
  --sessionId TEXT
  --userId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --help                      Show this message and exit.
```

### GetSessionUserExtendedDetailedUsage

```
Usage: panopto UsageReporting GetSessionUserExtendedDetailedUsage 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userId TEXT
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --help                      Show this message and exit.
```

### DescribeReportTypes

```
Usage: panopto UsageReporting DescribeReportTypes [OPTIONS]

Options:
  --help  Show this message and exit.
```

### DescribeReportType

```
Usage: panopto UsageReporting DescribeReportType [OPTIONS]

Options:
  --reportType TEXT
  --help             Show this message and exit.
```

### GetRecentReports

```
Usage: panopto UsageReporting GetRecentReports [OPTIONS]

Options:
  --reportType TEXT
  --help             Show this message and exit.
```

### QueueReport

```
Usage: panopto UsageReporting QueueReport [OPTIONS]

Options:
  --reportType TEXT
  --startTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.
```

### GetReport

```
Usage: panopto UsageReporting GetReport [OPTIONS]

Options:
  --reportId TEXT
  --help           Show this message and exit.
```

## UserManagement

### CreateUser

```
Usage: panopto UserManagement CreateUser [OPTIONS]

Options:
  --user TEXT
  --initialPassword TEXT
  --help                  Show this message and exit.
```

### CreateUsers

```
Usage: panopto UserManagement CreateUsers [OPTIONS]

Options:
  --users TEXT
  --help        Show this message and exit.
```

### GetUserByKey

```
Usage: panopto UserManagement GetUserByKey [OPTIONS]

Options:
  --userKey TEXT
  --help          Show this message and exit.
```

### GetUsers

```
Usage: panopto UserManagement GetUsers [OPTIONS]

Options:
  --userIds TEXT
  --help          Show this message and exit.
```

### ListUsers

```
Usage: panopto UserManagement ListUsers [OPTIONS]

Options:
  --parameters TEXT
  --searchQuery TEXT
  --help              Show this message and exit.
```

### UpdateContactInfo

```
Usage: panopto UserManagement UpdateContactInfo [OPTIONS]

Options:
  --userId TEXT
  --firstName TEXT
  --lastName TEXT
  --email TEXT
  --sendNotifications TEXT
  --help                    Show this message and exit.
```

### UpdateUserBio

```
Usage: panopto UserManagement UpdateUserBio [OPTIONS]

Options:
  --userId TEXT
  --bio TEXT
  --help         Show this message and exit.
```

### UpdatePassword

```
Usage: panopto UserManagement UpdatePassword [OPTIONS]

Options:
  --userId TEXT
  --newPassword TEXT
  --help              Show this message and exit.
```

### ResetPassword

```
Usage: panopto UserManagement ResetPassword [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.
```

### UnlockAccount

```
Usage: panopto UserManagement UnlockAccount [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.
```

### SetSystemRole

```
Usage: panopto UserManagement SetSystemRole [OPTIONS]

Options:
  --userId TEXT
  --role TEXT
  --help         Show this message and exit.
```

### DeleteUsers

```
Usage: panopto UserManagement DeleteUsers [OPTIONS]

Options:
  --userIds TEXT
  --help          Show this message and exit.
 ```
 
 ### CreateInternalGroup
 
 ```
 Usage: panopto UserManagement CreateInternalGroup [OPTIONS]

Options:
  --groupName TEXT
  --memberIds TEXT
  --help            Show this message and exit.
```

### GetGroupIsPublic

```
Usage: panopto UserManagement GetGroupIsPublic [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.
```

### SetGroupIsPublic

```
Usage: panopto UserManagement SetGroupIsPublic [OPTIONS]

Options:
  --groupId TEXT
  --isPublic TEXT
  --help           Show this message and exit.
```

### CreateExternalGroup

```
Usage: panopto UserManagement CreateExternalGroup [OPTIONS]

Options:
  --groupName TEXT
  --externalProvider TEXT
  --externalId TEXT
  --memberIds TEXT
  --help                   Show this message and exit.
 ```
 
 ### AddMembersToInternalGroup
 
 ```
 Usage: panopto UserManagement AddMembersToInternalGroup [OPTIONS]

Options:
  --groupId TEXT
  --memberIds TEXT
  --help            Show this message and exit.
```

### RemoveMembersFromInternalGroup

```
Usage: panopto UserManagement RemoveMembersFromInternalGroup 
           [OPTIONS]

Options:
  --groupId TEXT
  --memberIds TEXT
  --help            Show this message and exit.
```

### AddMembersToExternalGroup

```
Usage: panopto UserManagement AddMembersToExternalGroup [OPTIONS]

Options:
  --externalProviderName TEXT
  --externalGroupId TEXT
  --memberIds TEXT
  --help                       Show this message and exit.
```

### RemoveMembersFromExternalGroup

```
Usage: panopto UserManagement RemoveMembersFromExternalGroup 
           [OPTIONS]

Options:
  --externalProviderName TEXT
  --externalGroupId TEXT
  --memberIds TEXT
  --help                       Show this message and exit.
```

### SyncExternalUser

```
Usage: panopto UserManagement SyncExternalUser [OPTIONS]

Options:
  --firstName TEXT
  --lastName TEXT
  --email TEXT
  --EmailSessionNotifications TEXT
  --externalGroupIds TEXT
  --help                          Show this message and exit.
```

### DeleteGroup

```Usage: panopto UserManagement DeleteGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.
```

### GetGroup
 
```
Usage: panopto UserManagement GetGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.
 ```
 
 ### ListGroups
 
```
Usage: panopto UserManagement ListGroups [OPTIONS]

Options:
  --PageNumber INTEGER
  --MaxNumberResults INTEGER
  --help                      Show this message and exit.
```

### GetGroupsByName

```
Usage: panopto UserManagement GetGroupsByName [OPTIONS]

Options:
  --groupName TEXT
  --help            Show this message and exit.
```

### GetUsersInGroup

```
Usage: panopto UserManagement GetUsersInGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.
 ```
 
### SetUserHasLoggedIn

```
Usage: panopto UserManagement SetUserHasLoggedIn [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.
```
