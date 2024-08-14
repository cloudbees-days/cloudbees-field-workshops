procedure 'CreateUser', {
  description = ''
  jobNameTemplate = ''
  projectName = 'Workshop'
  resourceName = 'k8s-agent'
  timeLimit = '0'
  timeLimitUnits = 'minutes'
  workspaceName = ''

  formalParameter 'username', defaultValue: null, {
    expansionDeferred = '0'
    label = null
    orderIndex = '1'
    required = '1'
    type = 'entry'
  }

  formalParameter 'password', defaultValue: null, {
    expansionDeferred = '0'
    label = null
    orderIndex = '2'
    required = '1'
    type = 'entry'
  }

  step 'CreateUser', {
    description = ''
    alwaysRun = '0'
    broadcast = '0'
    command = '''ectool createUser $[username] --groupNames workshopUsers --personas WorkshopPeople --password $[password]
ectool createProject $[username]'''
    condition = ''
    errorHandling = 'failProcedure'
    exclusiveMode = 'none'
    logFileName = ''
    parallel = '0'
    postProcessor = ''
    precondition = ''
    procedureName = 'CreateUser'
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

  step 'CreateNamespaces', {
    description = ''
    alwaysRun = '0'
    broadcast = '0'
    command = '''echo "Create QA $[username]-qa"
kubectl create namespace $[username]-qa
echo "Create PROD $[username]-prod"
kubectl create namespace $[username]-prod'''
    condition = ''
    errorHandling = 'failProcedure'
    exclusiveMode = 'none'
    logFileName = ''
    parallel = '0'
    postProcessor = ''
    precondition = ''
    procedureName = 'CreateUser'
    releaseMode = 'none'
    resourceName = 'k8s-agent'
    shell = ''
    subprocedure = ''
    subproject = ''
    timeLimit = '0'
    timeLimitUnits = 'seconds'
    workingDirectory = ''
    workspaceName = ''
  }
}