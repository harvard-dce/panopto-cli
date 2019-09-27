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
	* [ReplaceMachineCaptionsAndUploadTranscript](#panopto-SessionManagement-ReplaceMachineCaptionsAndUploadTranscript)
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
	* [CancelReport](#panopto-UsageReporting-CancelReport)
	* [CreateRecurringReport](#panopto-UsageReporting-CreateRecurringReport)
	* [DeleteRecurringReport](#panopto-UsageReporting-DeleteRecurringReport)
	* [GetRecurringReports](#panopto-UsageReporting-GetRecurringReports)
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
  configure

```

### panopto AccessManagement
```
Usage: panopto AccessManagement [OPTIONS] COMMAND [ARGS]...

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
Usage: panopto AccessManagement GetUserAccessDetails [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

##### panopto AccessManagement GetSelfUserAccessDetails
```
Usage: panopto AccessManagement GetSelfUserAccessDetails [OPTIONS]

Options:
  --help  Show this message and exit.

```

##### panopto AccessManagement GetSessionAccessDetails
```
Usage: panopto AccessManagement GetSessionAccessDetails [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto AccessManagement GetFolderAccessDetails
```
Usage: panopto AccessManagement GetFolderAccessDetails [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.

```

##### panopto AccessManagement GetGroupAccessDetails
```
Usage: panopto AccessManagement GetGroupAccessDetails [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto AccessManagement GrantUsersAccessToFolder
```
Usage: panopto AccessManagement GrantUsersAccessToFolder [OPTIONS]

Options:
  --folderId TEXT
  --userIds TEXT                  allows multiple
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantUsersViewerAccessToSession
```
Usage: panopto AccessManagement GrantUsersViewerAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userIds TEXT    allows multiple
  --help            Show this message and exit.

```

##### panopto AccessManagement GrantGroupAccessToFolder
```
Usage: panopto AccessManagement GrantGroupAccessToFolder [OPTIONS]

Options:
  --folderId TEXT
  --groupId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantGroupViewerAccessToSession
```
Usage: panopto AccessManagement GrantGroupViewerAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --groupId TEXT
  --help            Show this message and exit.

```

##### panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToFolder
```
Usage: panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToSession
```
Usage: panopto AccessManagement GrantAllAuthenticatedUsersGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantPublicGroupAccessToFolder
```
Usage: panopto AccessManagement GrantPublicGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement GrantPublicGroupAccessToSession
```
Usage: panopto AccessManagement GrantPublicGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement RevokeAllImplicitGroupAccessToFolder
```
Usage: panopto AccessManagement RevokeAllImplicitGroupAccessToFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.

```

##### panopto AccessManagement RevokeAllImplicitGroupAccessToSession
```
Usage: panopto AccessManagement RevokeAllImplicitGroupAccessToSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto AccessManagement UpdateFolderIsPublic
```
Usage: panopto AccessManagement UpdateFolderIsPublic [OPTIONS]

Options:
  --folderId TEXT
  --isPublic BOOLEAN  true|false
  --help              Show this message and exit.

```

##### panopto AccessManagement UpdateSessionIsPublic
```
Usage: panopto AccessManagement UpdateSessionIsPublic [OPTIONS]

Options:
  --sessionId TEXT
  --isPublic BOOLEAN  true|false
  --help              Show this message and exit.

```

##### panopto AccessManagement UpdateSessionInheritViewerAccess
```
Usage: panopto AccessManagement UpdateSessionInheritViewerAccess 
           [OPTIONS]

Options:
  --sessionId TEXT
  --inheritViewerAccess BOOLEAN  true|false
  --help                         Show this message and exit.

```

##### panopto AccessManagement RevokeUsersAccessFromFolder
```
Usage: panopto AccessManagement RevokeUsersAccessFromFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --userIds TEXT                  allows multiple
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement RevokeUsersViewerAccessFromSession
```
Usage: panopto AccessManagement RevokeUsersViewerAccessFromSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userIds TEXT    allows multiple
  --help            Show this message and exit.

```

##### panopto AccessManagement RevokeGroupAccessFromFolder
```
Usage: panopto AccessManagement RevokeGroupAccessFromFolder 
           [OPTIONS]

Options:
  --folderId TEXT
  --groupId TEXT
  --role [Creator|Viewer|ViewerWithLink|Publisher]
  --help                          Show this message and exit.

```

##### panopto AccessManagement RevokeGroupViewerAccessFromSession
```
Usage: panopto AccessManagement RevokeGroupViewerAccessFromSession 
           [OPTIONS]

Options:
  --sessionId TEXT
  --groupId TEXT
  --help            Show this message and exit.

```

### panopto RemoteRecorderManagement
```
Usage: panopto RemoteRecorderManagement [OPTIONS] COMMAND [ARGS]...

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
Usage: panopto RemoteRecorderManagement GetRemoteRecordersById 
           [OPTIONS]

Options:
  --remoteRecorderIds TEXT  allows multiple
  --help                    Show this message and exit.

```

##### panopto RemoteRecorderManagement GetRemoteRecordersByExternalId
```
Usage: panopto RemoteRecorderManagement GetRemoteRecordersByExternalId 
           [OPTIONS]

Options:
  --externalIds TEXT  allows multiple
  --help              Show this message and exit.

```

##### panopto RemoteRecorderManagement UpdateRemoteRecorderExternalId
```
Usage: panopto RemoteRecorderManagement UpdateRemoteRecorderExternalId 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --externalId TEXT
  --help                   Show this message and exit.

```

##### panopto RemoteRecorderManagement ListRecorders
```
Usage: panopto RemoteRecorderManagement ListRecorders [OPTIONS]

Options:
  --pagination TEXT      format: MaxNumberResults=int,PageNumber=int
  --sortBy [Name|State]
  --help                 Show this message and exit.

```

##### panopto RemoteRecorderManagement ScheduleRecording
```
Usage: panopto RemoteRecorderManagement ScheduleRecording [OPTIONS]

Options:
  --name TEXT
  --folderId TEXT
  --isBroadcast BOOLEAN           true|false
  --start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --recorderSettings TEXT         allows multiple;
                                  format: RecorderId=guid,Sup
                                  pressPrimary=boolean,SuppressSecondary=boole
                                  an
  --help                          Show this message and exit.

```

##### panopto RemoteRecorderManagement ScheduleRecurringRecording
```
Usage: panopto RemoteRecorderManagement ScheduleRecurringRecording 
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
Usage: panopto RemoteRecorderManagement UpdateRecordingTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --start [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --end [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto RemoteRecorderManagement UpdateRecordingSettings
```
Usage: panopto RemoteRecorderManagement UpdateRecordingSettings 
           [OPTIONS]

Options:
  --sessionId TEXT
  --recorderSettings TEXT  allows multiple;
                           format: RecorderId=guid,SuppressPr
                           imary=boolean,SuppressSecondary=boolean
  --help                   Show this message and exit.

```

##### panopto RemoteRecorderManagement GetDefaultFolderForRecorder
```
Usage: panopto RemoteRecorderManagement GetDefaultFolderForRecorder 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --help                   Show this message and exit.

```

##### panopto RemoteRecorderManagement GetMachineSidForRecorder
```
Usage: panopto RemoteRecorderManagement GetMachineSidForRecorder 
           [OPTIONS]

Options:
  --remoteRecorderId TEXT
  --help                   Show this message and exit.

```

### panopto SessionManagement
```
Usage: panopto SessionManagement [OPTIONS] COMMAND [ARGS]...

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
  ReplaceMachineCaptionsAndUploadTranscript
  GetFoldersAvailabilitySettings
  GetSessionsAvailabilitySettings
  UpdateFoldersAvailabilityStartSettings
  UpdateFoldersAvailabilityEndSettings
  UpdateSessionsAvailabilityStartSettings
  UpdateSessionsAvailabilityEndSettings
  GetPersonalFolderForUser
  GetVideoDownloadURL
  UnprovisionExternalCourse
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
  ReplaceMachineCaptionsAndUploadTranscript
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
Usage: panopto SessionManagement AddFolder [OPTIONS]

Options:
  --name TEXT
  --parentFolder TEXT
  --isPublic BOOLEAN   true|false
  --help               Show this message and exit.

```

##### panopto SessionManagement AddSession
```
Usage: panopto SessionManagement AddSession [OPTIONS]

Options:
  --name TEXT
  --folderId TEXT
  --isBroadcast BOOLEAN  true|false
  --help                 Show this message and exit.

```

##### panopto SessionManagement GetFoldersById
```
Usage: panopto SessionManagement GetFoldersById [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement GetFoldersWithExternalContextById
```
Usage: panopto SessionManagement GetFoldersWithExternalContextById 
           [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement GetFoldersByExternalId
```
Usage: panopto SessionManagement GetFoldersByExternalId [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetFoldersWithExternalContextByExternalId
```
Usage: panopto SessionManagement GetFoldersWithExternalContextByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetAllFoldersByExternalId
```
Usage: panopto SessionManagement GetAllFoldersByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --providerNames TEXT      allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetAllFoldersWithExternalContextByExternalId
```
Usage: panopto SessionManagement GetAllFoldersWithExternalContextByExternalId 
           [OPTIONS]

Options:
  --folderExternalIds TEXT  allows multiple
  --providerNames TEXT      allows multiple
  --help                    Show this message and exit.

```

##### panopto SessionManagement GetSessionsById
```
Usage: panopto SessionManagement GetSessionsById [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement GetSessionsByExternalId
```
Usage: panopto SessionManagement GetSessionsByExternalId [OPTIONS]

Options:
  --sessionExternalIds TEXT  allows multiple
  --help                     Show this message and exit.

```

##### panopto SessionManagement GetSessionsList
```
Usage: panopto SessionManagement GetSessionsList [OPTIONS]

Options:
  --request TEXT      format: EndDate=dateTime,FolderId=guid,Pagination=Pagina
                      tion,RemoteRecorderId=guid,SortBy=SessionSortField,SortI
                      ncreasing=boolean,StartDate=dateTime,States=ArrayOfSessi
                      onState
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement GetFoldersList
```
Usage: panopto SessionManagement GetFoldersList [OPTIONS]

Options:
  --request TEXT      format: Pagination=Pagination,ParentFolderId=guid,Public
                      Only=boolean,SortBy=FolderSortField,SortIncreasing=boole
                      an,WildcardSearchNameOnly=boolean
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement GetFoldersWithExternalContextList
```
Usage: panopto SessionManagement GetFoldersWithExternalContextList 
           [OPTIONS]

Options:
  --request TEXT      format: Pagination=Pagination,ParentFolderId=guid,Public
                      Only=boolean,SortBy=FolderSortField,SortIncreasing=boole
                      an,WildcardSearchNameOnly=boolean
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement GetCreatorFoldersList
```
Usage: panopto SessionManagement GetCreatorFoldersList [OPTIONS]

Options:
  --request TEXT      format: Pagination=Pagination,ParentFolderId=guid,Public
                      Only=boolean,SortBy=FolderSortField,SortIncreasing=boole
                      an,WildcardSearchNameOnly=boolean
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement GetCreatorFoldersWithExternalContextList
```
Usage: panopto SessionManagement GetCreatorFoldersWithExternalContextList 
           [OPTIONS]

Options:
  --request TEXT      format: Pagination=Pagination,ParentFolderId=guid,Public
                      Only=boolean,SortBy=FolderSortField,SortIncreasing=boole
                      an,WildcardSearchNameOnly=boolean
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement UpdateSessionName
```
Usage: panopto SessionManagement UpdateSessionName [OPTIONS]

Options:
  --sessionId TEXT
  --name TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UpdateSessionDescription
```
Usage: panopto SessionManagement UpdateSessionDescription [OPTIONS]

Options:
  --sessionId TEXT
  --description TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement UpdateSessionIsBroadcast
```
Usage: panopto SessionManagement UpdateSessionIsBroadcast [OPTIONS]

Options:
  --sessionId TEXT
  --isBroadcast BOOLEAN  true|false
  --help                 Show this message and exit.

```

##### panopto SessionManagement UpdateSessionSetPanoptoBroadcast
```
Usage: panopto SessionManagement UpdateSessionSetPanoptoBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UpdateSessionSetRTMPBroadcast
```
Usage: panopto SessionManagement UpdateSessionSetRTMPBroadcast 
           [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UpdateSessionCreateRTMPStreams
```
Usage: panopto SessionManagement UpdateSessionCreateRTMPStreams 
           [OPTIONS]

Options:
  --sessionId TEXT
  --countToAdd INTEGER
  --arePrimaries BOOLEAN  true|false
  --help                  Show this message and exit.

```

##### panopto SessionManagement UpdateSessionUpdateRTMPStreamTypes
```
Usage: panopto SessionManagement UpdateSessionUpdateRTMPStreamTypes 
           [OPTIONS]

Options:
  --sessionId TEXT
  --streamKeys TEXT         allows multiple
  --setAsPrimaries BOOLEAN  true|false
  --help                    Show this message and exit.

```

##### panopto SessionManagement UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand
```
Usage: panopto SessionManagement UpdateSessionUpdateRTMPStreamSetShouldConvertToOnDemand 
           [OPTIONS]

Options:
  --sessionId TEXT
  --streamKeys TEXT  allows multiple
  --enabled BOOLEAN  true|false
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateSessionOwner
```
Usage: panopto SessionManagement UpdateSessionOwner [OPTIONS]

Options:
  --sessionIds TEXT       allows multiple
  --newOwnerUserKey TEXT
  --help                  Show this message and exit.

```

##### panopto SessionManagement MoveSessions
```
Usage: panopto SessionManagement MoveSessions [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --folderId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateSessionExternalId
```
Usage: panopto SessionManagement UpdateSessionExternalId [OPTIONS]

Options:
  --sessionId TEXT
  --externalId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateFolderName
```
Usage: panopto SessionManagement UpdateFolderName [OPTIONS]

Options:
  --folderId TEXT
  --name TEXT
  --help           Show this message and exit.

```

##### panopto SessionManagement UpdateFolderDescription
```
Usage: panopto SessionManagement UpdateFolderDescription [OPTIONS]

Options:
  --folderId TEXT
  --description TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement UpdateFolderEnablePodcast
```
Usage: panopto SessionManagement UpdateFolderEnablePodcast 
           [OPTIONS]

Options:
  --folderId TEXT
  --enablePodcast BOOLEAN  true|false
  --help                   Show this message and exit.

```

##### panopto SessionManagement UpdateFolderAllowPublicNotes
```
Usage: panopto SessionManagement UpdateFolderAllowPublicNotes 
           [OPTIONS]

Options:
  --folderId TEXT
  --allowPublicNotes BOOLEAN  true|false
  --help                      Show this message and exit.

```

##### panopto SessionManagement UpdateFolderAllowSessionDownload
```
Usage: panopto SessionManagement UpdateFolderAllowSessionDownload 
           [OPTIONS]

Options:
  --folderId TEXT
  --allowSessionDownload BOOLEAN  true|false
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateFolderParent
```
Usage: panopto SessionManagement UpdateFolderParent [OPTIONS]

Options:
  --folderId TEXT
  --parentId TEXT
  --help           Show this message and exit.

```

##### panopto SessionManagement UpdateFolderExternalId
```
Usage: panopto SessionManagement UpdateFolderExternalId [OPTIONS]

Options:
  --folderId TEXT
  --externalId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateFolderExternalIdWithProvider
```
Usage: panopto SessionManagement UpdateFolderExternalIdWithProvider 
           [OPTIONS]

Options:
  --folderId TEXT
  --externalId TEXT
  --SiteMembershipProviderName TEXT
  --help                          Show this message and exit.

```

##### panopto SessionManagement DeleteSessions
```
Usage: panopto SessionManagement DeleteSessions [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement DeleteFolders
```
Usage: panopto SessionManagement DeleteFolders [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement ProvisionExternalCourse
```
Usage: panopto SessionManagement ProvisionExternalCourse [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --help             Show this message and exit.

```

##### panopto SessionManagement EnsureExternalHierarchyBranch
```
Usage: panopto SessionManagement EnsureExternalHierarchyBranch 
           [OPTIONS]

Options:
  --externalHierarchyBranch TEXT  allows multiple;
                                  format: ExternalId=string,I
                                  sCourse=boolean,Name=string
  --help                          Show this message and exit.

```

##### panopto SessionManagement ProvisionExternalCourseWithRoles
```
Usage: panopto SessionManagement ProvisionExternalCourseWithRoles 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --roles TEXT       allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetExternalCourseAccess
```
Usage: panopto SessionManagement SetExternalCourseAccess [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT   allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetExternalCourseAccessForRoles
```
Usage: panopto SessionManagement SetExternalCourseAccessForRoles 
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
Usage: panopto SessionManagement SetCopiedExternalCourseAccess 
           [OPTIONS]

Options:
  --name TEXT
  --externalId TEXT
  --folderIds TEXT   allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement SetCopiedExternalCourseAccessForRoles
```
Usage: panopto SessionManagement SetCopiedExternalCourseAccessForRoles 
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
Usage: panopto SessionManagement GetRecorderDownloadUrls [OPTIONS]

Options:
  --help  Show this message and exit.

```

##### panopto SessionManagement CreateNoteByRelativeTime
```
Usage: panopto SessionManagement CreateNoteByRelativeTime [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --channel TEXT
  --timestamp FLOAT
  --help             Show this message and exit.

```

##### panopto SessionManagement CreateNoteByAbsoluteTime
```
Usage: panopto SessionManagement CreateNoteByAbsoluteTime [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --channel TEXT
  --timestamp [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement EditNote
```
Usage: panopto SessionManagement EditNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --newText TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement DeleteNote
```
Usage: panopto SessionManagement DeleteNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement GetNote
```
Usage: panopto SessionManagement GetNote [OPTIONS]

Options:
  --noteId TEXT
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement ListNotes
```
Usage: panopto SessionManagement ListNotes [OPTIONS]

Options:
  --sessionId TEXT
  --pagination TEXT   format: MaxNumberResults=int,PageNumber=int
  --creatorId TEXT
  --channel TEXT
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto SessionManagement AreUsersNotesPublic
```
Usage: panopto SessionManagement AreUsersNotesPublic [OPTIONS]

Options:
  --userId TEXT
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement SetNotesPublic
```
Usage: panopto SessionManagement SetNotesPublic [OPTIONS]

Options:
  --sessionId TEXT
  --areNotesPublic BOOLEAN  true|false
  --help                    Show this message and exit.

```

##### panopto SessionManagement IsDropbox
```
Usage: panopto SessionManagement IsDropbox [OPTIONS]

Options:
  --folderId TEXT
  --help           Show this message and exit.

```

##### panopto SessionManagement CreateCaptionByRelativeTime
```
Usage: panopto SessionManagement CreateCaptionByRelativeTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --timestamp FLOAT
  --help             Show this message and exit.

```

##### panopto SessionManagement CreateCaptionByAbsoluteTime
```
Usage: panopto SessionManagement CreateCaptionByAbsoluteTime 
           [OPTIONS]

Options:
  --sessionId TEXT
  --text TEXT
  --timestamp [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement UploadTranscript
```
Usage: panopto SessionManagement UploadTranscript [OPTIONS]

Options:
  --sessionId TEXT
  --file TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement ReplaceMachineCaptionsAndUploadTranscript
```
Usage: panopto SessionManagement ReplaceMachineCaptionsAndUploadTranscript 
           [OPTIONS]

Options:
  --sessionId TEXT
  --file TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement GetFoldersAvailabilitySettings
```
Usage: panopto SessionManagement GetFoldersAvailabilitySettings 
           [OPTIONS]

Options:
  --folderIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto SessionManagement GetSessionsAvailabilitySettings
```
Usage: panopto SessionManagement GetSessionsAvailabilitySettings 
           [OPTIONS]

Options:
  --sessionIds TEXT  allows multiple
  --help             Show this message and exit.

```

##### panopto SessionManagement UpdateFoldersAvailabilityStartSettings
```
Usage: panopto SessionManagement UpdateFoldersAvailabilityStartSettings 
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
Usage: panopto SessionManagement UpdateFoldersAvailabilityEndSettings 
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
Usage: panopto SessionManagement UpdateSessionsAvailabilityStartSettings 
           [OPTIONS]

Options:
  --sessionIds TEXT               allows multiple
  --settingType [Immediately|WithItsFolder|SpecificDate]
  --startDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement UpdateSessionsAvailabilityEndSettings
```
Usage: panopto SessionManagement UpdateSessionsAvailabilityEndSettings 
           [OPTIONS]

Options:
  --sessionIds TEXT               allows multiple
  --settingType [Forever|WithItsFolder|SpecificDate]
  --endDate [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto SessionManagement GetPersonalFolderForUser
```
Usage: panopto SessionManagement GetPersonalFolderForUser [OPTIONS]

Options:
  --userId TEXT
  --allowCreation BOOLEAN  true|false
  --help                   Show this message and exit.

```

##### panopto SessionManagement GetVideoDownloadURL
```
Usage: panopto SessionManagement GetVideoDownloadURL [OPTIONS]

Options:
  --sessionId TEXT
  --help            Show this message and exit.

```

##### panopto SessionManagement UnprovisionExternalCourse
```
Usage: panopto SessionManagement UnprovisionExternalCourse 
           [OPTIONS]

Options:
  --externalContextId TEXT
  --help                    Show this message and exit.

```

### panopto UsageReporting
```
Usage: panopto UsageReporting [OPTIONS] COMMAND [ARGS]...

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
  CancelReport
  CreateRecurringReport
  DeleteRecurringReport
  GetRecurringReports
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
  CancelReport
  CreateRecurringReport
  DeleteRecurringReport
  GetRecurringReports

```

##### panopto UsageReporting GetSystemSummaryUsage
```
Usage: panopto UsageReporting GetSystemSummaryUsage [OPTIONS]

Options:
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity [Hourly|Daily|Weekly]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetFolderSummaryUsage
```
Usage: panopto UsageReporting GetFolderSummaryUsage [OPTIONS]

Options:
  --folderId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity [Hourly|Daily|Weekly]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionSummaryUsage
```
Usage: panopto UsageReporting GetSessionSummaryUsage [OPTIONS]

Options:
  --sessionId TEXT
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --granularity [Hourly|Daily|Weekly]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionDetailedUsage
```
Usage: panopto UsageReporting GetSessionDetailedUsage [OPTIONS]

Options:
  --sessionId TEXT
  --pagination TEXT               format: MaxNumberResults=int,PageNumber=int
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionExtendedDetailedUsage
```
Usage: panopto UsageReporting GetSessionExtendedDetailedUsage 
           [OPTIONS]

Options:
  --sessionId TEXT
  --pagination TEXT               format: MaxNumberResults=int,PageNumber=int
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetUserDetailedUsage
```
Usage: panopto UsageReporting GetUserDetailedUsage [OPTIONS]

Options:
  --userId TEXT
  --pagination TEXT  format: MaxNumberResults=int,PageNumber=int
  --help             Show this message and exit.

```

##### panopto UsageReporting GetUserExtendedDetailedUsage
```
Usage: panopto UsageReporting GetUserExtendedDetailedUsage 
           [OPTIONS]

Options:
  --userId TEXT
  --pagination TEXT               format: MaxNumberResults=int,PageNumber=int
  --beginRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endRange [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetSessionUserDetailedUsage
```
Usage: panopto UsageReporting GetSessionUserDetailedUsage [OPTIONS]

Options:
  --sessionId TEXT
  --userId TEXT
  --pagination TEXT  format: MaxNumberResults=int,PageNumber=int
  --help             Show this message and exit.

```

##### panopto UsageReporting GetSessionUserExtendedDetailedUsage
```
Usage: panopto UsageReporting GetSessionUserExtendedDetailedUsage 
           [OPTIONS]

Options:
  --sessionId TEXT
  --userId TEXT
  --pagination TEXT  format: MaxNumberResults=int,PageNumber=int
  --help             Show this message and exit.

```

##### panopto UsageReporting DescribeReportTypes
```
Usage: panopto UsageReporting DescribeReportTypes [OPTIONS]

Options:
  --help  Show this message and exit.

```

##### panopto UsageReporting DescribeReportType
```
Usage: panopto UsageReporting DescribeReportType [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetRecentReports
```
Usage: panopto UsageReporting GetRecentReports [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --help                          Show this message and exit.

```

##### panopto UsageReporting QueueReport
```
Usage: panopto UsageReporting QueueReport [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --startTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --endTime [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
  --help                          Show this message and exit.

```

##### panopto UsageReporting GetReport
```
Usage: panopto UsageReporting GetReport [OPTIONS]

Options:
  --reportId TEXT
  --help           Show this message and exit.

```

##### panopto UsageReporting CancelReport
```
Usage: panopto UsageReporting CancelReport [OPTIONS]

Options:
  --reportId TEXT
  --help           Show this message and exit.

```

##### panopto UsageReporting CreateRecurringReport
```
Usage: panopto UsageReporting CreateRecurringReport [OPTIONS]

Options:
  --cadenceType TEXT
  --cadenceOffset INTEGER
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --help                          Show this message and exit.

```

##### panopto UsageReporting DeleteRecurringReport
```
Usage: panopto UsageReporting DeleteRecurringReport [OPTIONS]

Options:
  --reportId TEXT
  --help           Show this message and exit.

```

##### panopto UsageReporting GetRecurringReports
```
Usage: panopto UsageReporting GetRecurringReports [OPTIONS]

Options:
  --reportType [FolderUsage|SessionUsage|UserViewingUsage|UserCreationUsage|LastLoginTime|SessionsViewsByUsers|SessionsViewsByViewingType|SessionsCreatedOrEdited|RemoteRecorderUsage|SystemViews]
  --help                          Show this message and exit.

```

### panopto UserManagement
```
Usage: panopto UserManagement [OPTIONS] COMMAND [ARGS]...

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
Usage: panopto UserManagement CreateUser [OPTIONS]

Options:
  --user TEXT             format: Email=string,EmailSessionNotifications=boole
                          an,FirstName=string,GroupMemberships=ArrayOfguid,Las
                          tName=string,SystemRole=SystemRole,UserBio=string,Us
                          erId=guid,UserKey=string,UserSettingsUrl=string
  --initialPassword TEXT
  --help                  Show this message and exit.

```

##### panopto UserManagement CreateUsers
```
Usage: panopto UserManagement CreateUsers [OPTIONS]

Options:
  --users TEXT  allows multiple;
                format: Email=string,EmailSessionNotification
                s=boolean,FirstName=string,GroupMemberships=ArrayOfguid,LastNa
                me=string,SystemRole=SystemRole,UserBio=string,UserId=guid,Use
                rKey=string,UserSettingsUrl=string
  --help        Show this message and exit.

```

##### panopto UserManagement GetUserByKey
```
Usage: panopto UserManagement GetUserByKey [OPTIONS]

Options:
  --userKey TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement GetUsers
```
Usage: panopto UserManagement GetUsers [OPTIONS]

Options:
  --userIds TEXT  allows multiple
  --help          Show this message and exit.

```

##### panopto UserManagement ListUsers
```
Usage: panopto UserManagement ListUsers [OPTIONS]

Options:
  --parameters TEXT   format: Pagination=Pagination,SortBy=UserSortField,SortI
                      ncreasing=boolean
  --searchQuery TEXT
  --help              Show this message and exit.

```

##### panopto UserManagement UpdateContactInfo
```
Usage: panopto UserManagement UpdateContactInfo [OPTIONS]

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
Usage: panopto UserManagement UpdateUserBio [OPTIONS]

Options:
  --userId TEXT
  --bio TEXT
  --help         Show this message and exit.

```

##### panopto UserManagement UpdatePassword
```
Usage: panopto UserManagement UpdatePassword [OPTIONS]

Options:
  --userId TEXT
  --newPassword TEXT
  --help              Show this message and exit.

```

##### panopto UserManagement ResetPassword
```
Usage: panopto UserManagement ResetPassword [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

##### panopto UserManagement UnlockAccount
```
Usage: panopto UserManagement UnlockAccount [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

##### panopto UserManagement SetSystemRole
```
Usage: panopto UserManagement SetSystemRole [OPTIONS]

Options:
  --userId TEXT
  --role [None|Videographer|Admin]
  --help                          Show this message and exit.

```

##### panopto UserManagement DeleteUsers
```
Usage: panopto UserManagement DeleteUsers [OPTIONS]

Options:
  --userIds TEXT  allows multiple
  --help          Show this message and exit.

```

##### panopto UserManagement CreateInternalGroup
```
Usage: panopto UserManagement CreateInternalGroup [OPTIONS]

Options:
  --groupName TEXT
  --memberIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto UserManagement GetGroupIsPublic
```
Usage: panopto UserManagement GetGroupIsPublic [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement SetGroupIsPublic
```
Usage: panopto UserManagement SetGroupIsPublic [OPTIONS]

Options:
  --groupId TEXT
  --isPublic BOOLEAN  true|false
  --help              Show this message and exit.

```

##### panopto UserManagement CreateExternalGroup
```
Usage: panopto UserManagement CreateExternalGroup [OPTIONS]

Options:
  --groupName TEXT
  --externalProvider TEXT
  --externalId TEXT
  --memberIds TEXT         allows multiple
  --help                   Show this message and exit.

```

##### panopto UserManagement AddMembersToInternalGroup
```
Usage: panopto UserManagement AddMembersToInternalGroup [OPTIONS]

Options:
  --groupId TEXT
  --memberIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto UserManagement RemoveMembersFromInternalGroup
```
Usage: panopto UserManagement RemoveMembersFromInternalGroup 
           [OPTIONS]

Options:
  --groupId TEXT
  --memberIds TEXT  allows multiple
  --help            Show this message and exit.

```

##### panopto UserManagement AddMembersToExternalGroup
```
Usage: panopto UserManagement AddMembersToExternalGroup [OPTIONS]

Options:
  --externalProviderName TEXT
  --externalGroupId TEXT
  --memberIds TEXT             allows multiple
  --help                       Show this message and exit.

```

##### panopto UserManagement RemoveMembersFromExternalGroup
```
Usage: panopto UserManagement RemoveMembersFromExternalGroup 
           [OPTIONS]

Options:
  --externalProviderName TEXT
  --externalGroupId TEXT
  --memberIds TEXT             allows multiple
  --help                       Show this message and exit.

```

##### panopto UserManagement SyncExternalUser
```
Usage: panopto UserManagement SyncExternalUser [OPTIONS]

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
Usage: panopto UserManagement DeleteGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement GetGroup
```
Usage: panopto UserManagement GetGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement ListGroups
```
Usage: panopto UserManagement ListGroups [OPTIONS]

Options:
  --pagination TEXT  format: MaxNumberResults=int,PageNumber=int
  --help             Show this message and exit.

```

##### panopto UserManagement GetGroupsByName
```
Usage: panopto UserManagement GetGroupsByName [OPTIONS]

Options:
  --groupName TEXT
  --help            Show this message and exit.

```

##### panopto UserManagement GetUsersInGroup
```
Usage: panopto UserManagement GetUsersInGroup [OPTIONS]

Options:
  --groupId TEXT
  --help          Show this message and exit.

```

##### panopto UserManagement SetUserHasLoggedIn
```
Usage: panopto UserManagement SetUserHasLoggedIn [OPTIONS]

Options:
  --userId TEXT
  --help         Show this message and exit.

```

