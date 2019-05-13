* [AccessManagement](#panopto-AccessManagement)
	* [GetUserAccessDetails](#panopto-AccessManagement-GetUserAccessDetails)
	* [GetSelfUserAccessDetails](#panopto-AccessManagement-GetSelfUserAccessDetails)
	* [GetSessionAccessDetails](#panopto-AccessManagement-GetSessionAccessDetails)
	* [GetFolderAccessDetails](#panopto-AccessManagement-GetFolderAccessDetails)
	* [GetGroupAccessDetails](#panopto-AccessManagement-GetGroupAccessDetails)
	* [GrantUsersAccessToFolder](#panopto-AccessManagement-GrantUsersAccessToFolder)
	* [GrantUsersViewerAccessToSession](#panopto-AccessManagement-GrantUsersViewerAccessToSession)
	* [GrantGroupAccessToFolder](#panopto-AccessManagement-GrantGroupAccessToFolder)
	* [GrantGroupViewerAccessToSession](#panopto-AccessManagement-GrantGroupViewerAccessToSession)
	* [GrantAllAuthenticatedUsersGroupAccessToFolder](#panopto-AccessManagement-GrantAllAuthenticatedUsersGroupAccessToFolder)
	* [GrantAllAuthenticatedUsersGroupAccessToSession](#panopto-AccessManagement-GrantAllAuthenticatedUsersGroupAccessToSession)
	* [GrantPublicGroupAccessToFolder](#panopto-AccessManagement-GrantPublicGroupAccessToFolder)
	* [GrantPublicGroupAccessToSession](#panopto-AccessManagement-GrantPublicGroupAccessToSession)
	* [RevokeAllImplicitGroupAccessToFolder](#panopto-AccessManagement-RevokeAllImplicitGroupAccessToFolder)
	* [RevokeAllImplicitGroupAccessToSession](#panopto-AccessManagement-RevokeAllImplicitGroupAccessToSession)
	* [UpdateFolderIsPublic](#panopto-AccessManagement-UpdateFolderIsPublic)
	* [UpdateSessionIsPublic](#panopto-AccessManagement-UpdateSessionIsPublic)
	* [UpdateSessionInheritViewerAccess](#panopto-AccessManagement-UpdateSessionInheritViewerAccess)
	* [RevokeUsersAccessFromFolder](#panopto-AccessManagement-RevokeUsersAccessFromFolder)
	* [RevokeUsersViewerAccessFromSession](#panopto-AccessManagement-RevokeUsersViewerAccessFromSession)
	* [RevokeGroupAccessFromFolder](#panopto-AccessManagement-RevokeGroupAccessFromFolder)
	* [RevokeGroupViewerAccessFromSession](#panopto-AccessManagement-RevokeGroupViewerAccessFromSession)
* [RemoteRecorderManagement](#panopto-RemoteRecorderManagement)
	* [GetRemoteRecordersById](#panopto-RemoteRecorderManagement-GetRemoteRecordersById)
	* [GetRemoteRecordersByExternalId](#panopto-RemoteRecorderManagement-GetRemoteRecordersByExternalId)
	* [UpdateRemoteRecorderExternalId](#panopto-RemoteRecorderManagement-UpdateRemoteRecorderExternalId)
	* [ListRecorders](#panopto-RemoteRecorderManagement-ListRecorders)
	* [ScheduleRecording](#panopto-RemoteRecorderManagement-ScheduleRecording)
	* [ScheduleRecurringRecording](#panopto-RemoteRecorderManagement-ScheduleRecurringRecording)
	* [UpdateRecordingTime](#panopto-RemoteRecorderManagement-UpdateRecordingTime)
	* [UpdateRecordingSettings](#panopto-RemoteRecorderManagement-UpdateRecordingSettings)
	* [GetDefaultFolderForRecorder](#panopto-RemoteRecorderManagement-GetDefaultFolderForRecorder)
	* [GetMachineSidForRecorder](#panopto-RemoteRecorderManagement-GetMachineSidForRecorder)
* [SessionManagement](#panopto-SessionManagement)
	* [AddFolder](#panopto-SessionManagement-AddFolder)
	* [AddSession](#panopto-SessionManagement-AddSession)
	* [GetFoldersById](#panopto-SessionManagement-GetFoldersById)
	* [GetFoldersWithExternalContextById](#panopto-SessionManagement-GetFoldersWithExternalContextById)
	* [GetFoldersByExternalId](#panopto-SessionManagement-GetFoldersByExternalId)
	* [GetFoldersWithExternalContextByExternalId](#panopto-SessionManagement-GetFoldersWithExternalContextByExternalId)
	* [GetAllFoldersByExternalId](#panopto-SessionManagement-GetAllFoldersByExternalId)
	* [GetAllFoldersWithExternalContextByExternalId](#panopto-SessionManagement-GetAllFoldersWithExternalContextByExternalId)
	* [GetSessionsById](#panopto-SessionManagement-GetSessionsById)
	* [GetSessionsByExternalId](#panopto-SessionManagement-GetSessionsByExternalId)
	* [GetSessionsList](#panopto-SessionManagement-GetSessionsList)
	* [GetFoldersList](#panopto-SessionManagement-GetFoldersList)
	* [GetFoldersWithExternalContextList](#panopto-SessionManagement-GetFoldersWithExternalContextList)
	* [GetCreatorFoldersList](#panopto-SessionManagement-GetCreatorFoldersList)
	* [GetCreatorFoldersWithExternalContextList](#panopto-SessionManagement-GetCreatorFoldersWithExternalContextList)
	* [UpdateSessionName](#panopto-SessionManagement-UpdateSessionName)
	* [UpdateSessionDescription](#panopto-SessionManagement-UpdateSessionDescription)
	* [UpdateSessionIsBroadcast](#panopto-SessionManagement-UpdateSessionIsBroadcast)
	* [UpdateSessionSetPanoptoBroadcast](#panopto-SessionManagement-UpdateSessionSetPanoptoBroadcast)
	* [UpdateSessionSetRTMPBroadcast](#panopto-SessionManagement-UpdateSessionSetRTMPBroadcast)
	* [UpdateSessionCreateRTMPStreams](#panopto-SessionManagement-UpdateSessionCreateRTMPStreams)
	* [UpdateSessionUpdateRTMPStreamTypes](#panopto-SessionManagement-UpdateSessionUpdateRTMPStreamTypes)
	* [UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand](#panopto-SessionManagement-UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand)
	* [UpdateSessionOwner](#panopto-SessionManagement-UpdateSessionOwner)
	* [MoveSessions](#panopto-SessionManagement-MoveSessions)
	* [UpdateSessionExternalId](#panopto-SessionManagement-UpdateSessionExternalId)
	* [UpdateFolderName](#panopto-SessionManagement-UpdateFolderName)
	* [UpdateFolderDescription](#panopto-SessionManagement-UpdateFolderDescription)
	* [UpdateFolderEnablePodcast](#panopto-SessionManagement-UpdateFolderEnablePodcast)
	* [UpdateFolderAllowPublicNotes](#panopto-SessionManagement-UpdateFolderAllowPublicNotes)
	* [UpdateFolderAllowSessionDownload](#panopto-SessionManagement-UpdateFolderAllowSessionDownload)
	* [UpdateFolderParent](#panopto-SessionManagement-UpdateFolderParent)
	* [UpdateFolderExternalId](#panopto-SessionManagement-UpdateFolderExternalId)
	* [UpdateFolderExternalIdWithProvider](#panopto-SessionManagement-UpdateFolderExternalIdWithProvider)
	* [DeleteSessions](#panopto-SessionManagement-DeleteSessions)
	* [DeleteFolders](#panopto-SessionManagement-DeleteFolders)
	* [ProvisionExternalCourse](#panopto-SessionManagement-ProvisionExternalCourse)
	* [EnsureExternalHierarchyBranch](#panopto-SessionManagement-EnsureExternalHierarchyBranch)
	* [ProvisionExternalCourseWithRoles](#panopto-SessionManagement-ProvisionExternalCourseWithRoles)
	* [SetExternalCourseAccess](#panopto-SessionManagement-SetExternalCourseAccess)
	* [SetExternalCourseAccessForRoles](#panopto-SessionManagement-SetExternalCourseAccessForRoles)
	* [SetCopiedExternalCourseAccess](#panopto-SessionManagement-SetCopiedExternalCourseAccess)
	* [SetCopiedExternalCourseAccessForRoles](#panopto-SessionManagement-SetCopiedExternalCourseAccessForRoles)
	* [GetRecorderDownloadUrls](#panopto-SessionManagement-GetRecorderDownloadUrls)
	* [CreateNoteByRelativeTime](#panopto-SessionManagement-CreateNoteByRelativeTime)
	* [CreateNoteByAbsoluteTime](#panopto-SessionManagement-CreateNoteByAbsoluteTime)
	* [EditNote](#panopto-SessionManagement-EditNote)
	* [DeleteNote](#panopto-SessionManagement-DeleteNote)
	* [GetNote](#panopto-SessionManagement-GetNote)
	* [ListNotes](#panopto-SessionManagement-ListNotes)
	* [AreUsersNotesPublic](#panopto-SessionManagement-AreUsersNotesPublic)
	* [SetNotesPublic](#panopto-SessionManagement-SetNotesPublic)
	* [IsDropbox](#panopto-SessionManagement-IsDropbox)
	* [CreateCaptionByRelativeTime](#panopto-SessionManagement-CreateCaptionByRelativeTime)
	* [CreateCaptionByAbsoluteTime](#panopto-SessionManagement-CreateCaptionByAbsoluteTime)
	* [UploadTranscript](#panopto-SessionManagement-UploadTranscript)
	* [GetFoldersAvailabilitySettings](#panopto-SessionManagement-GetFoldersAvailabilitySettings)
	* [GetSessionsAvailabilitySettings](#panopto-SessionManagement-GetSessionsAvailabilitySettings)
	* [UpdateFoldersAvailabilityStartSettings](#panopto-SessionManagement-UpdateFoldersAvailabilityStartSettings)
	* [UpdateFoldersAvailabilityEndSettings](#panopto-SessionManagement-UpdateFoldersAvailabilityEndSettings)
	* [UpdateSessionsAvailabilityStartSettings](#panopto-SessionManagement-UpdateSessionsAvailabilityStartSettings)
	* [UpdateSessionsAvailabilityEndSettings](#panopto-SessionManagement-UpdateSessionsAvailabilityEndSettings)
	* [GetPersonalFolderForUser](#panopto-SessionManagement-GetPersonalFolderForUser)
	* [GetVideoDownloadURL](#panopto-SessionManagement-GetVideoDownloadURL)
	* [UnprovisionExternalCourse](#panopto-SessionManagement-UnprovisionExternalCourse)
* [UsageReporting](#panopto-UsageReporting)
	* [GetSystemSummaryUsage](#panopto-UsageReporting-GetSystemSummaryUsage)
	* [GetFolderSummaryUsage](#panopto-UsageReporting-GetFolderSummaryUsage)
	* [GetSessionSummaryUsage](#panopto-UsageReporting-GetSessionSummaryUsage)
	* [GetSessionDetailedUsage](#panopto-UsageReporting-GetSessionDetailedUsage)
	* [GetSessionExtendedDetailedUsage](#panopto-UsageReporting-GetSessionExtendedDetailedUsage)
	* [GetUserDetailedUsage](#panopto-UsageReporting-GetUserDetailedUsage)
	* [GetUserExtendedDetailedUsage](#panopto-UsageReporting-GetUserExtendedDetailedUsage)
	* [GetSessionUserDetailedUsage](#panopto-UsageReporting-GetSessionUserDetailedUsage)
	* [GetSessionUserExtendedDetailedUsage](#panopto-UsageReporting-GetSessionUserExtendedDetailedUsage)
	* [DescribeReportTypes](#panopto-UsageReporting-DescribeReportTypes)
	* [DescribeReportType](#panopto-UsageReporting-DescribeReportType)
	* [GetRecentReports](#panopto-UsageReporting-GetRecentReports)
	* [QueueReport](#panopto-UsageReporting-QueueReport)
	* [GetReport](#panopto-UsageReporting-GetReport)
* [UserManagement](#panopto-UserManagement)
	* [CreateUser](#panopto-UserManagement-CreateUser)
	* [CreateUsers](#panopto-UserManagement-CreateUsers)
	* [GetUserByKey](#panopto-UserManagement-GetUserByKey)
	* [GetUsers](#panopto-UserManagement-GetUsers)
	* [ListUsers](#panopto-UserManagement-ListUsers)
	* [UpdateContactInfo](#panopto-UserManagement-UpdateContactInfo)
	* [UpdateUserBio](#panopto-UserManagement-UpdateUserBio)
	* [UpdatePassword](#panopto-UserManagement-UpdatePassword)
	* [ResetPassword](#panopto-UserManagement-ResetPassword)
	* [UnlockAccount](#panopto-UserManagement-UnlockAccount)
	* [SetSystemRole](#panopto-UserManagement-SetSystemRole)
	* [DeleteUsers](#panopto-UserManagement-DeleteUsers)
	* [CreateInternalGroup](#panopto-UserManagement-CreateInternalGroup)
	* [GetGroupIsPublic](#panopto-UserManagement-GetGroupIsPublic)
	* [SetGroupIsPublic](#panopto-UserManagement-SetGroupIsPublic)
	* [CreateExternalGroup](#panopto-UserManagement-CreateExternalGroup)
	* [AddMembersToInternalGroup](#panopto-UserManagement-AddMembersToInternalGroup)
	* [RemoveMembersFromInternalGroup](#panopto-UserManagement-RemoveMembersFromInternalGroup)
	* [AddMembersToExternalGroup](#panopto-UserManagement-AddMembersToExternalGroup)
	* [RemoveMembersFromExternalGroup](#panopto-UserManagement-RemoveMembersFromExternalGroup)
	* [SyncExternalUser](#panopto-UserManagement-SyncExternalUser)
	* [DeleteGroup](#panopto-UserManagement-DeleteGroup)
	* [GetGroup](#panopto-UserManagement-GetGroup)
	* [ListGroups](#panopto-UserManagement-ListGroups)
	* [GetGroupsByName](#panopto-UserManagement-GetGroupsByName)
	* [GetUsersInGroup](#panopto-UserManagement-GetUsersInGroup)
	* [SetUserHasLoggedIn](#panopto-UserManagement-SetUserHasLoggedIn)




## panopto 
```
Usage: panopto.py [OPTIONS] COMMAND [ARGS]...

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

### panopto AccessManagement
```
Usage: panopto.py AccessManagement [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  GetUserAccessDetails
  GetSelfUserAccessDetails
  GetSessionAccessDetails
  GetFolderAccessDetails
  GetGroupAccessDetails
  GrantUsersAccessToFolder
  GrantUsersViewerAccessToSession
  GrantGroupAccessToFolder
  GrantGroupViewerAccessToSession
  GrantAllAuthenticatedUsersGroupAccessToFolder
  GrantAllAuthenticatedUsersGroupAccessToSession
  GrantPublicGroupAccessToFolder
  GrantPublicGroupAccessToSession
  RevokeAllImplicitGroupAccessToFolder
  RevokeAllImplicitGroupAccessToSession
  UpdateFolderIsPublic
  UpdateSessionIsPublic
  UpdateSessionInheritViewerAccess
  RevokeUsersAccessFromFolder
  RevokeUsersViewerAccessFromSession
  RevokeGroupAccessFromFolder
  RevokeGroupViewerAccessFromSession

```

##### panopto AccessManagement GetUserAccessDetails
```
Usage: panopto.py AccessManagement GetUserAccessDetails [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

##### panopto AccessManagement GetSelfUserAccessDetails
```
Usage: panopto.py AccessManagement GetSelfUserAccessDetails 
           [OPTIONS]

Options:
  --help  Show this message and exit.

```

##### panopto AccessManagement GetSessionAccessDetails
```
Usage: panopto.py AccessManagement GetSessionAccessDetails 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto AccessManagement GetFolderAccessDetails
```
Usage: panopto.py AccessManagement GetFolderAccessDetails [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.

```

##### panopto AccessManagement GetGroupAccessDetails
```
Usage: panopto.py AccessManagement GetGroupAccessDetails [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto AccessManagement GrantUsersAccessToFolder
```
Usage: panopto.py AccessManagement GrantUsersAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --userIds TEXT                  allows multiple
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantUsersViewerAccessToSession
```
Usage: panopto.py AccessManagement GrantUsersViewerAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userIds TEXT    allows multiple
  --help            Show this message and exit.

```

##### panopto AccessManagement GrantGroupAccessToFolder
```
Usage: panopto.py AccessManagement GrantGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --groupId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantGroupViewerAccessToSession
```
Usage: panopto.py AccessManagement GrantGroupViewerAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --groupId TEXT
  --help            Show this message and exit.

```

##### panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToFolder
```
Usage: panopto.py AccessManagement GrantAllAuthenticatedUsersGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToSession
```
Usage: panopto.py AccessManagement GrantAllAuthenticatedUsersGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantPublicGroupAccessToFolder
```
Usage: panopto.py AccessManagement GrantPublicGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantPublicGroupAccessToSession
```
Usage: panopto.py AccessManagement GrantPublicGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement RevokeAllImplicitGroupAccessToFolder
```
Usage: panopto.py AccessManagement RevokeAllImplicitGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.

```

##### panopto AccessManagement RevokeAllImplicitGroupAccessToSession
```
Usage: panopto.py AccessManagement RevokeAllImplicitGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto AccessManagement UpdateFolderIsPublic
```
Usage: panopto.py AccessManagement UpdateFolderIsPublic [OPTIONS]

Options:
  --folderId TEXT
  --isPublic BOOLEAN  true|false
  --help              Show this message and exit.

```

##### panopto AccessManagement UpdateSessionIsPublic
```
Usage: panopto.py AccessManagement UpdateSessionIsPublic [OPTIONS]

Options:
  --sessionId TEXT
  --isPublic BOOLEAN  true|false
  --help              Show this message and exit.

```

##### panopto AccessManagement UpdateSessionInheritViewerAccess
```
Usage: panopto.py AccessManagement UpdateSessionInheritViewerAccess 
           [OPTIONS]

Options:
  --sessionId TEXT
  --inheritViewerAccess BOOLEAN  true|false
  --help                         Show this message and exit.

```

##### panopto AccessManagement RevokeUsersAccessFromFolder
```
Usage: panopto.py AccessManagement RevokeUsersAccessFromFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --userIds TEXT                  allows multiple
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement RevokeUsersViewerAccessFromSession
```
Usage: panopto.py AccessManagement RevokeUsersViewerAccessFromSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userIds TEXT    allows multiple
  --help            Show this message and exit.

```

##### panopto AccessManagement RevokeGroupAccessFromFolder
```
Usage: panopto.py AccessManagement RevokeGroupAccessFromFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --groupId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement RevokeGroupViewerAccessFromSession
```
Usage: panopto.py AccessManagement RevokeGroupViewerAccessFromSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --groupId TEXT
  --help            Show this message and exit.

```

### panopto RemoteRecorderManagement
```
Usage: panopto.py RemoteRecorderManagement [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  GetRemoteRecordersById
  GetRemoteRecordersByExternalId
  UpdateRemoteRecorderExternalId
  ListRecorders
  ScheduleRecording
  ScheduleRecurringRecording
  UpdateRecordingTime
  UpdateRecordingSettings
  GetDefaultFolderForRecorder
  GetMachineSidForRecorder

```

##### panopto RemoteRecorderManagement GetRemoteRecordersById
```
Usage: panopto.py RemoteRecorderManagement GetRemoteRecordersById 
           [OPTIONS]

Options:
  --remoteRecorderIds TEXT  allows multiple
  --help                    Show this message and exit.

```

##### panopto RemoteRecorderManagement GetRemoteRecordersByExternalId
```
Usage: panopto.py RemoteRecorderManagement GetRemoteRecordersByExternalId 
           [OPTIONS]

Options:
  --externalIds TEXT  allows multiple
  --help              Show this message and exit.

```

##### panopto RemoteRecorderManagement UpdateRemoteRecorderExternalId
```
Usage: panopto.py RemoteRecorderManagement UpdateRemoteRecorderExternalId 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --externalId TEXT
  --help                   Show this message and exit.

```

##### panopto RemoteRecorderManagement ListRecorders
```
Usage: panopto.py RemoteRecorderManagement ListRecorders [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --sortBy [Name|State]
  --help                      Show this message and exit.

```

##### panopto RemoteRecorderManagement ScheduleRecording
```
Usage: panopto.py RemoteRecorderManagement ScheduleRecording 
           [OPTIONS]

Options:
  --name TEXT
  --folderId TEXT
  --isBroadcast BOOLEAN           true|false
  --start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --recorderSettings TEXT         allows multiple
  --help                          Show this message and exit.

```

##### panopto RemoteRecorderManagement ScheduleRecurringRecording
```
Usage: panopto.py RemoteRecorderManagement ScheduleRecurringRecording 
           [OPTIONS]

Options:
  --scheduledSessionId TEXT
  --daysOfWeek [Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday]
                                  allows multiple
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto RemoteRecorderManagement UpdateRecordingTime
```
Usage: panopto.py RemoteRecorderManagement UpdateRecordingTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto RemoteRecorderManagement UpdateRecordingSettings
```
Usage: panopto.py RemoteRecorderManagement UpdateRecordingSettings 
           [OPTIONS]

Options:
  --sessionId TEXT
  --recorderSettings TEXT  allows multiple
  --help                   Show this message and exit.

```

##### panopto RemoteRecorderManagement GetDefaultFolderForRecorder
```
Usage: panopto.py RemoteRecorderManagement GetDefaultFolderForRecorder 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --help                   Show this message and exit.

```

##### panopto RemoteRecorderManagement GetMachineSidForRecorder
```
Usage: panopto.py RemoteRecorderManagement GetMachineSidForRecorder 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --help                   Show this message and exit.

```

### panopto SessionManagement
```
Usage: panopto.py SessionManagement [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  AddFolder
  AddSession
  GetFoldersById
  GetFoldersWithExternalContextById
  GetFoldersByExternalId
  GetFoldersWithExternalContextByExternalId
  GetAllFoldersByExternalId
  GetAllFoldersWithExternalContextByExternalId
  GetSessionsById
  GetSessionsByExternalId
  GetSessionsList
  GetFoldersList
  GetFoldersWithExternalContextList
  GetCreatorFoldersList
  GetCreatorFoldersWithExternalContextList
  UpdateSessionName
  UpdateSessionDescription
  UpdateSessionIsBroadcast
  UpdateSessionSetPanoptoBroadcast
  UpdateSessionSetRTMPBroadcast
  UpdateSessionCreateRTMPStreams
  UpdateSessionUpdateRTMPStreamTypes
  UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand
  UpdateSessionOwner
  MoveSessions
  UpdateSessionExternalId
  UpdateFolderName
  UpdateFolderDescription
  UpdateFolderEnablePodcast
  UpdateFolderAllowPublicNotes
  UpdateFolderAllowSessionDownload
  UpdateFolderParent
  UpdateFolderExternalId
  UpdateFolderExternalIdWithProvider
  DeleteSessions
  DeleteFolders
  ProvisionExternalCourse
  EnsureExternalHierarchyBranch
  ProvisionExternalCourseWithRoles
  SetExternalCourseAccess
  SetExternalCourseAccessForRoles
  SetCopiedExternalCourseAccess
  SetCopiedExternalCourseAccessForRoles
  GetRecorderDownloadUrls
  CreateNoteByRelativeTime
  CreateNoteByAbsoluteTime
  EditNote
  DeleteNote
  GetNote
  ListNotes
  AreUsersNotesPublic
  SetNotesPublic
  IsDropbox
  CreateCaptionByRelativeTime
  CreateCaptionByAbsoluteTime
  UploadTranscript
  GetFoldersAvailabilitySettings
  GetSessionsAvailabilitySettings
  UpdateFoldersAvailabilityStartSettings
  UpdateFoldersAvailabilityEndSettings
  UpdateSessionsAvailabilityStartSettings
  UpdateSessionsAvailabilityEndSettings
  GetPersonalFolderForUser
  GetVideoDownloadURL
  UnprovisionExternalCourse

```

##### panopto SessionManagement AddFolder
```
Usage: panopto.py SessionManagement AddFolder [OPTIONS]

Options:
  --name TEXT
  --parentFolder TEXT
  --isPublic BOOLEAN   true|false
  --help               Show this message and exit.

```

##### panopto SessionManagement AddSession
```
Usage: panopto.py SessionManagement AddSession [OPTIONS]

Options:
  --name TEXT
  --folderId TEXT
  --isBroadcast BOOLEAN  true|false
  --help                 Show this message and exit.

```

##### panopto SessionManagement GetFoldersById
```
Usage: panopto.py SessionManagement GetFoldersById [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement GetFoldersWithExternalContextById
```
Usage: panopto.py SessionManagement GetFoldersWithExternalContextById 
           [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement GetFoldersByExternalId
```
Usage: panopto.py SessionManagement GetFoldersByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetFoldersWithExternalContextByExternalId
```
Usage: panopto.py SessionManagement GetFoldersWithExternalContextByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetAllFoldersByExternalId
```
Usage: panopto.py SessionManagement GetAllFoldersByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --providerNames TEXT      allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetAllFoldersWithExternalContextByExternalId
```
Usage: panopto.py SessionManagement GetAllFoldersWithExternalContextByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --providerNames TEXT      allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetSessionsById
```
Usage: panopto.py SessionManagement GetSessionsById [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement GetSessionsByExternalId
```
Usage: panopto.py SessionManagement GetSessionsByExternalId 
           [OPTIONS]

Options:
  --sessionExternalIds TEXT  allows multiple
  --help                     Show this message and exit.

```

##### panopto SessionManagement GetSessionsList
```
Usage: panopto.py SessionManagement GetSessionsList [OPTIONS]

Options:
  --EndDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --FolderId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --RemoteRecorderId TEXT
  --SortBy [Name|Date|Duration|State|Relevance|Order]
  --SortIncreasing BOOLEAN        true|false
  --StartDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --States TEXT                   allows multiple
  --searchQuery TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement GetFoldersList
```
Usage: panopto.py SessionManagement GetFoldersList [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --ParentFolderId TEXT
  --PublicOnly BOOLEAN            true|false
  --SortBy [Name|Sessions|Relavance]
  --SortIncreasing BOOLEAN        true|false
  --WildcardSearchNameOnly BOOLEAN
                                  true|false
  --searchQuery TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement GetFoldersWithExternalContextList
```
Usage: panopto.py SessionManagement GetFoldersWithExternalContextList 
           [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --ParentFolderId TEXT
  --PublicOnly BOOLEAN            true|false
  --SortBy [Name|Sessions|Relavance]
  --SortIncreasing BOOLEAN        true|false
  --WildcardSearchNameOnly BOOLEAN
                                  true|false
  --searchQuery TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement GetCreatorFoldersList
```
Usage: panopto.py SessionManagement GetCreatorFoldersList [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --ParentFolderId TEXT
  --PublicOnly BOOLEAN            true|false
  --SortBy [Name|Sessions|Relavance]
  --SortIncreasing BOOLEAN        true|false
  --WildcardSearchNameOnly BOOLEAN
                                  true|false
  --searchQuery TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement GetCreatorFoldersWithExternalContextList
```
Usage: panopto.py SessionManagement GetCreatorFoldersWithExternalContextList 
           [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --ParentFolderId TEXT
  --PublicOnly BOOLEAN            true|false
  --SortBy [Name|Sessions|Relavance]
  --SortIncreasing BOOLEAN        true|false
  --WildcardSearchNameOnly BOOLEAN
                                  true|false
  --searchQuery TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateSessionName
```
Usage: panopto.py SessionManagement UpdateSessionName [OPTIONS]

Options:
  --sessionId TEXT
  --name TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UpdateSessionDescription
```
Usage: panopto.py SessionManagement UpdateSessionDescription 
           [OPTIONS]

Options:
  --sessionId TEXT
  --description TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement UpdateSessionIsBroadcast
```
Usage: panopto.py SessionManagement UpdateSessionIsBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --isBroadcast BOOLEAN  true|false
  --help                 Show this message and exit.

```

##### panopto SessionManagement UpdateSessionSetPanoptoBroadcast
```
Usage: panopto.py SessionManagement UpdateSessionSetPanoptoBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UpdateSessionSetRTMPBroadcast
```
Usage: panopto.py SessionManagement UpdateSessionSetRTMPBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UpdateSessionCreateRTMPStreams
```
Usage: panopto.py SessionManagement UpdateSessionCreateRTMPStreams 
           [OPTIONS]

Options:
  --sessionId TEXT
  --countToAdd INTEGER
  --arePrimaries BOOLEAN  true|false
  --help                  Show this message and exit.

```

##### panopto SessionManagement UpdateSessionUpdateRTMPStreamTypes
```
Usage: panopto.py SessionManagement UpdateSessionUpdateRTMPStreamTypes 
           [OPTIONS]

Options:
  --sessionId TEXT
  --streamKeys TEXT         allows multiple
  --setAsPrimaries BOOLEAN  true|false
  --help                    Show this message and exit.

```

##### panopto SessionManagement UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand
```
Usage: panopto.py SessionManagement UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand 
           [OPTIONS]

Options:
  --sessionId TEXT
  --streamKeys TEXT  allows multiple
  --enabled BOOLEAN  true|false
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateSessionOwner
```
Usage: panopto.py SessionManagement UpdateSessionOwner [OPTIONS]

Options:
  --sessionIds TEXT       allows multiple
  --newOwnerUserKey TEXT
  --help                  Show this message and exit.

```

##### panopto SessionManagement MoveSessions
```
Usage: panopto.py SessionManagement MoveSessions [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --folderId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateSessionExternalId
```
Usage: panopto.py SessionManagement UpdateSessionExternalId 
           [OPTIONS]

Options:
  --sessionId TEXT
  --externalId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateFolderName
```
Usage: panopto.py SessionManagement UpdateFolderName [OPTIONS]

Options:
  --folderId TEXT
  --name TEXT
  --help           Show this message and exit.

```

##### panopto SessionManagement UpdateFolderDescription
```
Usage: panopto.py SessionManagement UpdateFolderDescription 
           [OPTIONS]

Options:
  --folderId TEXT
  --description TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement UpdateFolderEnablePodcast
```
Usage: panopto.py SessionManagement UpdateFolderEnablePodcast 
           [OPTIONS]

Options:
  --folderId TEXT
  --enablePodcast BOOLEAN  true|false
  --help                   Show this message and exit.

```

##### panopto SessionManagement UpdateFolderAllowPublicNotes
```
Usage: panopto.py SessionManagement UpdateFolderAllowPublicNotes 
           [OPTIONS]

Options:
  --folderId TEXT
  --allowPublicNotes BOOLEAN  true|false
  --help                      Show this message and exit.

```

##### panopto SessionManagement UpdateFolderAllowSessionDownload
```
Usage: panopto.py SessionManagement UpdateFolderAllowSessionDownload 
           [OPTIONS]

Options:
  --folderId TEXT
  --allowSessionDownload BOOLEAN  true|false
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateFolderParent
```
Usage: panopto.py SessionManagement UpdateFolderParent [OPTIONS]

Options:
  --folderId TEXT
  --parentId TEXT
  --help           Show this message and exit.

```

##### panopto SessionManagement UpdateFolderExternalId
```
Usage: panopto.py SessionManagement UpdateFolderExternalId 
           [OPTIONS]

Options:
  --folderId TEXT
  --externalId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateFolderExternalIdWithProvider
```
Usage: panopto.py SessionManagement UpdateFolderExternalIdWithProvider 
           [OPTIONS]

Options:
  --folderId TEXT
  --externalId TEXT
  --SiteMembershipProviderName TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement DeleteSessions
```
Usage: panopto.py SessionManagement DeleteSessions [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement DeleteFolders
```
Usage: panopto.py SessionManagement DeleteFolders [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement ProvisionExternalCourse
```
Usage: panopto.py SessionManagement ProvisionExternalCourse 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement EnsureExternalHierarchyBranch
```
Usage: panopto.py SessionManagement EnsureExternalHierarchyBranch 
           [OPTIONS]

Options:
  --externalHierarchyBranch TEXT  allows multiple
  --help                          Show this message and exit.

```

##### panopto SessionManagement ProvisionExternalCourseWithRoles
```
Usage: panopto.py SessionManagement ProvisionExternalCourseWithRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --roles TEXT       allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetExternalCourseAccess
```
Usage: panopto.py SessionManagement SetExternalCourseAccess 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT   allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetExternalCourseAccessForRoles
```
Usage: panopto.py SessionManagement SetExternalCourseAccessForRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT   allows multiple
  --roles TEXT       allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetCopiedExternalCourseAccess
```
Usage: panopto.py SessionManagement SetCopiedExternalCourseAccess 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT   allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetCopiedExternalCourseAccessForRoles
```
Usage: panopto.py SessionManagement SetCopiedExternalCourseAccessForRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT   allows multiple
  --roles TEXT       allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement GetRecorderDownloadUrls
```
Usage: panopto.py SessionManagement GetRecorderDownloadUrls 
           [OPTIONS]

Options:
  --help  Show this message and exit.

```

##### panopto SessionManagement CreateNoteByRelativeTime
```
Usage: panopto.py SessionManagement CreateNoteByRelativeTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --channel TEXT
  --timestamp FLOAT
  --help             Show this message and exit.

```

##### panopto SessionManagement CreateNoteByAbsoluteTime
```
Usage: panopto.py SessionManagement CreateNoteByAbsoluteTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --channel TEXT
  --timestamp [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement EditNote
```
Usage: panopto.py SessionManagement EditNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --newText TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement DeleteNote
```
Usage: panopto.py SessionManagement DeleteNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement GetNote
```
Usage: panopto.py SessionManagement GetNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement ListNotes
```
Usage: panopto.py SessionManagement ListNotes [OPTIONS]

Options:
  --sessionId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --creatorId TEXT
  --channel TEXT
  --searchQuery TEXT
  --help                      Show this message and exit.

```

##### panopto SessionManagement AreUsersNotesPublic
```
Usage: panopto.py SessionManagement AreUsersNotesPublic [OPTIONS]

Options:
  --userId TEXT
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement SetNotesPublic
```
Usage: panopto.py SessionManagement SetNotesPublic [OPTIONS]

Options:
  --sessionId TEXT
  --areNotesPublic BOOLEAN  true|false
  --help                    Show this message and exit.

```

##### panopto SessionManagement IsDropbox
```
Usage: panopto.py SessionManagement IsDropbox [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.

```

##### panopto SessionManagement CreateCaptionByRelativeTime
```
Usage: panopto.py SessionManagement CreateCaptionByRelativeTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --timestamp FLOAT
  --help             Show this message and exit.

```

##### panopto SessionManagement CreateCaptionByAbsoluteTime
```
Usage: panopto.py SessionManagement CreateCaptionByAbsoluteTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --timestamp [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement UploadTranscript
```
Usage: panopto.py SessionManagement UploadTranscript [OPTIONS]

Options:
  --sessionId TEXT
  --file TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement GetFoldersAvailabilitySettings
```
Usage: panopto.py SessionManagement GetFoldersAvailabilitySettings 
           [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement GetSessionsAvailabilitySettings
```
Usage: panopto.py SessionManagement GetSessionsAvailabilitySettings 
           [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateFoldersAvailabilityStartSettings
```
Usage: panopto.py SessionManagement UpdateFoldersAvailabilityStartSettings 
           [OPTIONS]

Options:
  --folderIds TEXT                allows multiple
  --settingType [Immediately|WhenPublisherApproved|NeverUnlessSessionSet|SpecificDate]
  --startDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --overrideSessionsSettings BOOLEAN
                                  true|false
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateFoldersAvailabilityEndSettings
```
Usage: panopto.py SessionManagement UpdateFoldersAvailabilityEndSettings 
           [OPTIONS]

Options:
  --folderIds TEXT                allows multiple
  --settingType TEXT
  --endDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --overrideSessionsSettings BOOLEAN
                                  true|false
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateSessionsAvailabilityStartSettings
```
Usage: panopto.py SessionManagement UpdateSessionsAvailabilityStartSettings 
           [OPTIONS]

Options:
  --sessionIds TEXT               allows multiple
  --settingType [Immediately|WithItsFolder|SpecificDate]
  --startDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateSessionsAvailabilityEndSettings
```
Usage: panopto.py SessionManagement UpdateSessionsAvailabilityEndSettings 
           [OPTIONS]

Options:
  --sessionIds TEXT               allows multiple
  --settingType [Forever|WithItsFolder|SpecificDate]
  --endDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement GetPersonalFolderForUser
```
Usage: panopto.py SessionManagement GetPersonalFolderForUser 
           [OPTIONS]

Options:
  --userId TEXT
  --allowCreation BOOLEAN  true|false
  --help                   Show this message and exit.

```

##### panopto SessionManagement GetVideoDownloadURL
```
Usage: panopto.py SessionManagement GetVideoDownloadURL [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UnprovisionExternalCourse
```
Usage: panopto.py SessionManagement UnprovisionExternalCourse 
           [OPTIONS]

Options:
  --externalContextId TEXT
  --help                    Show this message and exit.

```

### panopto UsageReporting
```
Usage: panopto.py UsageReporting [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  GetSystemSummaryUsage
  GetFolderSummaryUsage
  GetSessionSummaryUsage
  GetSessionDetailedUsage
  GetSessionExtendedDetailedUsage
  GetUserDetailedUsage
  GetUserExtendedDetailedUsage
  GetSessionUserDetailedUsage
  GetSessionUserExtendedDetailedUsage
  DescribeReportTypes
  DescribeReportType
  GetRecentReports
  QueueReport
  GetReport

```

##### panopto UsageReporting GetSystemSummaryUsage
```
Usage: panopto.py UsageReporting GetSystemSummaryUsage [OPTIONS]

Options:
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity [Hourly|Daily|Weekly]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetFolderSummaryUsage
```
Usage: panopto.py UsageReporting GetFolderSummaryUsage [OPTIONS]

Options:
  --folderId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity [Hourly|Daily|Weekly]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionSummaryUsage
```
Usage: panopto.py UsageReporting GetSessionSummaryUsage [OPTIONS]

Options:
  --sessionId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity [Hourly|Daily|Weekly]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionDetailedUsage
```
Usage: panopto.py UsageReporting GetSessionDetailedUsage [OPTIONS]

Options:
  --sessionId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionExtendedDetailedUsage
```
Usage: panopto.py UsageReporting GetSessionExtendedDetailedUsage 
           [OPTIONS]

Options:
  --sessionId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetUserDetailedUsage
```
Usage: panopto.py UsageReporting GetUserDetailedUsage [OPTIONS]

Options:
  --userId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --help                      Show this message and exit.

```

##### panopto UsageReporting GetUserExtendedDetailedUsage
```
Usage: panopto.py UsageReporting GetUserExtendedDetailedUsage 
           [OPTIONS]

Options:
  --userId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionUserDetailedUsage
```
Usage: panopto.py UsageReporting GetSessionUserDetailedUsage 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --help                      Show this message and exit.

```

##### panopto UsageReporting GetSessionUserExtendedDetailedUsage
```
Usage: panopto.py UsageReporting GetSessionUserExtendedDetailedUsage 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userId TEXT
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --help                      Show this message and exit.

```

##### panopto UsageReporting DescribeReportTypes
```
Usage: panopto.py UsageReporting DescribeReportTypes [OPTIONS]

Options:
  --help  Show this message and exit.

```

##### panopto UsageReporting DescribeReportType
```
Usage: panopto.py UsageReporting DescribeReportType [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetRecentReports
```
Usage: panopto.py UsageReporting GetRecentReports [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --help                          Show this message and exit.

```

##### panopto UsageReporting QueueReport
```
Usage: panopto.py UsageReporting QueueReport [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --startTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetReport
```
Usage: panopto.py UsageReporting GetReport [OPTIONS]

Options:
  --reportId TEXT
  --help           Show this message and exit.

```

### panopto UserManagement
```
Usage: panopto.py UserManagement [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  CreateUser
  CreateUsers
  GetUserByKey
  GetUsers
  ListUsers
  UpdateContactInfo
  UpdateUserBio
  UpdatePassword
  ResetPassword
  UnlockAccount
  SetSystemRole
  DeleteUsers
  CreateInternalGroup
  GetGroupIsPublic
  SetGroupIsPublic
  CreateExternalGroup
  AddMembersToInternalGroup
  RemoveMembersFromInternalGroup
  AddMembersToExternalGroup
  RemoveMembersFromExternalGroup
  SyncExternalUser
  DeleteGroup
  GetGroup
  ListGroups
  GetGroupsByName
  GetUsersInGroup
  SetUserHasLoggedIn

```

##### panopto UserManagement CreateUser
```
Usage: panopto.py UserManagement CreateUser [OPTIONS]

Options:
  --Email TEXT
  --EmailSessionNotifications BOOLEAN
                                  true|false
  --FirstName TEXT
  --GroupMemberships TEXT         allows multiple
  --LastName TEXT
  --SystemRole [None|Videographer|Admin]
  --UserBio TEXT
  --UserId TEXT
  --UserKey TEXT
  --UserSettingsUrl TEXT
  --initialPassword TEXT
  --help                          Show this message and exit.

```

##### panopto UserManagement CreateUsers
```
Usage: panopto.py UserManagement CreateUsers [OPTIONS]

Options:
  --users TEXT  allows multiple
  --help        Show this message and exit.

```

##### panopto UserManagement GetUserByKey
```
Usage: panopto.py UserManagement GetUserByKey [OPTIONS]

Options:
  --userKey TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement GetUsers
```
Usage: panopto.py UserManagement GetUsers [OPTIONS]

Options:
  --userIds TEXT  allows multiple
  --help          Show this message and exit.

```

##### panopto UserManagement ListUsers
```
Usage: panopto.py UserManagement ListUsers [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --SortBy [UserKey|Role|Added|LastLogOn|Email|FullName]
  --SortIncreasing BOOLEAN        true|false
  --searchQuery TEXT
  --help                          Show this message and exit.

```

##### panopto UserManagement UpdateContactInfo
```
Usage: panopto.py UserManagement UpdateContactInfo [OPTIONS]

Options:
  --userId TEXT
  --firstName TEXT
  --lastName TEXT
  --email TEXT
  --sendNotifications BOOLEAN  true|false
  --help                       Show this message and exit.

```

##### panopto UserManagement UpdateUserBio
```
Usage: panopto.py UserManagement UpdateUserBio [OPTIONS]

Options:
  --userId TEXT
  --bio TEXT
  --help         Show this message and exit.

```

##### panopto UserManagement UpdatePassword
```
Usage: panopto.py UserManagement UpdatePassword [OPTIONS]

Options:
  --userId TEXT
  --newPassword TEXT
  --help              Show this message and exit.

```

##### panopto UserManagement ResetPassword
```
Usage: panopto.py UserManagement ResetPassword [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

##### panopto UserManagement UnlockAccount
```
Usage: panopto.py UserManagement UnlockAccount [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

##### panopto UserManagement SetSystemRole
```
Usage: panopto.py UserManagement SetSystemRole [OPTIONS]

Options:
  --userId TEXT
  --role [None|Videographer|Admin]
  --help                          Show this message and exit.

```

##### panopto UserManagement DeleteUsers
```
Usage: panopto.py UserManagement DeleteUsers [OPTIONS]

Options:
  --userIds TEXT  allows multiple
  --help          Show this message and exit.

```

##### panopto UserManagement CreateInternalGroup
```
Usage: panopto.py UserManagement CreateInternalGroup [OPTIONS]

Options:
  --groupName TEXT
  --memberIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto UserManagement GetGroupIsPublic
```
Usage: panopto.py UserManagement GetGroupIsPublic [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement SetGroupIsPublic
```
Usage: panopto.py UserManagement SetGroupIsPublic [OPTIONS]

Options:
  --groupId TEXT
  --isPublic BOOLEAN  true|false
  --help              Show this message and exit.

```

##### panopto UserManagement CreateExternalGroup
```
Usage: panopto.py UserManagement CreateExternalGroup [OPTIONS]

Options:
  --groupName TEXT
  --externalProvider TEXT
  --externalId TEXT
  --memberIds TEXT         allows multiple
  --help                   Show this message and exit.

```

##### panopto UserManagement AddMembersToInternalGroup
```
Usage: panopto.py UserManagement AddMembersToInternalGroup 
           [OPTIONS]

Options:
  --groupId TEXT
  --memberIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto UserManagement RemoveMembersFromInternalGroup
```
Usage: panopto.py UserManagement RemoveMembersFromInternalGroup 
           [OPTIONS]

Options:
  --groupId TEXT
  --memberIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto UserManagement AddMembersToExternalGroup
```
Usage: panopto.py UserManagement AddMembersToExternalGroup 
           [OPTIONS]

Options:
  --externalProviderName TEXT
  --externalGroupId TEXT
  --memberIds TEXT             allows multiple
  --help                       Show this message and exit.

```

##### panopto UserManagement RemoveMembersFromExternalGroup
```
Usage: panopto.py UserManagement RemoveMembersFromExternalGroup 
           [OPTIONS]

Options:
  --externalProviderName TEXT
  --externalGroupId TEXT
  --memberIds TEXT             allows multiple
  --help                       Show this message and exit.

```

##### panopto UserManagement SyncExternalUser
```
Usage: panopto.py UserManagement SyncExternalUser [OPTIONS]

Options:
  --firstName TEXT
  --lastName TEXT
  --email TEXT
  --EmailSessionNotifications BOOLEAN
                                  true|false
  --externalGroupIds TEXT         allows multiple
  --help                          Show this message and exit.

```

##### panopto UserManagement DeleteGroup
```
Usage: panopto.py UserManagement DeleteGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement GetGroup
```
Usage: panopto.py UserManagement GetGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement ListGroups
```
Usage: panopto.py UserManagement ListGroups [OPTIONS]

Options:
  --MaxNumberResults INTEGER
  --PageNumber INTEGER
  --help                      Show this message and exit.

```

##### panopto UserManagement GetGroupsByName
```
Usage: panopto.py UserManagement GetGroupsByName [OPTIONS]

Options:
  --groupName TEXT
  --help            Show this message and exit.

```

##### panopto UserManagement GetUsersInGroup
```
Usage: panopto.py UserManagement GetUsersInGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement SetUserHasLoggedIn
```
Usage: panopto.py UserManagement SetUserHasLoggedIn [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

