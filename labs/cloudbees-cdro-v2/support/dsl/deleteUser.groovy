procedure 'DeleteUser', {
  description = ''
  jobNameTemplate = ''
  projectName = 'Workshop'
  resourceName = ''
  timeLimit = '0'
  timeLimitUnits = 'minutes'
  workspaceName = ''

  formalParameter 'username', defaultValue: '', {
    expansionDeferred = '0'
    label = null
    orderIndex = '1'
    required = '1'
    type = 'entry'
  }

  step 'deleteUser', {
    description = ''
    alwaysRun = '0'
    broadcast = '0'
    command = '''ectool deleteUser $[username]
ectool deleteProject $[username]'''
    condition = ''
    errorHandling = 'failProcedure'
    exclusiveMode = 'none'
    logFileName = ''
    parallel = '0'
    postProcessor = ''
    precondition = ''
    procedureName = 'DeleteUser'
    releaseMode = 'none'
    resourceName = ''
    shell = ''
    subprocedure = ''
    subproject = ''
    timeLimit = '0'
    timeLimitUnits = 'seconds'
    workingDirectory = ''
    workspaceName = ''
  }

  step 'deleteNamespaces', {
    description = ''
    alwaysRun = '0'
    broadcast = '0'
    command = '''echo "Delete QA $[username]-qa"
kubectl delete namespace $[username]-qa
echo "Delete PROD $[username]-prod"
kubectl delete namespace $[username]-prod'''
    condition = ''
    errorHandling = 'failProcedure'
    exclusiveMode = 'none'
    logFileName = ''
    parallel = '0'
    postProcessor = ''
    precondition = ''
    procedureName = 'DeleteUser'
    releaseMode = 'none'
    resourceName = ''
    shell = ''
    subprocedure = ''
    subproject = ''
    timeLimit = '0'
    timeLimitUnits = 'seconds'
    workingDirectory = ''
    workspaceName = ''
  }
}