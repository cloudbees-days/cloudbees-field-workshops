catalog 'Workshop', {
  projectName = 'Workshop'

  catalogItem '1. Basic Release', {
    description = '''<xml>
  <title>
    Create a new released based on pipeline templates
  </title>

  <htmlData>
    <![CDATA[
      Create a new release from existing pipeline templates
    ]]>
  </htmlData>
</xml>'''
    buttonLabel = 'Create'
    catalogName = 'Workshop'
    dslString = '''def StartDate = (new Date())
def StartDateStr = (String) StartDate.format( "yyyy-MM-dd" )
def EndDateStr = (String) (StartDate+14).format( "yyyy-MM-dd" )

release args.releaseName, {
  projectName = args.targetProject

  plannedStartDate = StartDateStr
  plannedEndDate = EndDateStr
  
  pipelineProjectName = "Workshop"
  pipelineName = "Pipeline_base"
  
  Release_Name = args.releaseTag
  String[] tags = args.releaseTag.replaceAll("[.]", "").split(", ");
  for (String tagItem: tags) {
    tag tagItem
  }
}'''
    endTargetJson = '''{
  "source": "parameter",
  "object": "release",
  "objectName": "releaseName",
  "objectProjectName": "targetProject",
  "objectId": "id"
}'''
    iconUrl = 'icon-pipeline.svg'
    useFormalParameter = '1'

    formalParameter 'releaseName', defaultValue: '$[/myUser/userName] Release', {
      label = 'Release Name'
      orderIndex = '1'
      required = '1'
      type = 'entry'
    }

    formalParameter 'releaseTag', defaultValue: 'PROD', {
      label = 'Release Tags'
      orderIndex = '2'
      required = '1'
      type = 'entry'
    }
    formalParameter 'targetProject', defaultValue: '$[/myUser/userName]', {
      expansionDeferred = '0'
      label = 'Target Project'
      orderIndex = '3'
      required = '1'
      type = 'project'
    }
  }
}