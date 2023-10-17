pipeline 'pipeline_Base', {
  projectName = 'Workshop'

  formalParameter 'ec_stagesToRun', {
    expansionDeferred = '1'
  }

  stage 'Release Readiness', {
    colorCode = '#289ce1'
    pipelineName = 'pipeline_Base'
    gate 'POST', {
      task 'No Code Smells', {
        gateCondition = '$[/javascript myStageRuntime.tasks[\'Get latest SonarQube scan results\'].job.getLastSonarMetrics.code_smells != null || myStageRuntime.tasks[\'Get latest SonarQube scan results\'].job.getLastSonarMetrics.code_smells < 1]'
        gateType = 'POST'
        subproject = 'Workshop'
        taskType = 'CONDITIONAL'
      }
    }

    task 'Git changelog', {
      actualParameter = [
        'branch': 'main',
        'commit': '',
        'config': '/projects/Workshop/pluginConfigurations/Git-Source-Code-Sync',
        'depth': '',
        'gitRepoFolder': '/tmp/demo-app',
        'mirror': 'false',
        'overwrite': 'true',
        'pathspecs': '',
        'referenceFolder': '',
        'repoUrl': 'https://github.com/cloudbees-days/cdro-workshop-demo-app',
        'resultPropertySheet': '/myJob/clone',
        'shallowSubmodules': 'false',
        'submodules': 'false',
        'tag': '',
      ]
      stageSummaryParameters = '[{"label":"cloneData","name":"cloneData"}]'
      subpluginKey = 'EC-Git'
      subprocedure = 'Clone'
      taskType = 'PLUGIN'
    }

    task 'Get latest SonarQube scan results', {
      actualParameter = [
        'config': '/projects/Workshop/pluginConfigurations/cb-demos-sonar',
        'resultFormat': 'propertysheet',
        'resultSonarProperty': '/myJob/getLastSonarMetrics',
        'sonarMetricsComplexity': 'all',
        'sonarMetricsDocumentation': 'all',
        'sonarMetricsDuplications': 'all',
        'sonarMetricsIssues': 'all',
        'sonarMetricsMaintainability': 'all',
        'sonarMetricsMetrics': 'all',
        'sonarMetricsQualityGates': 'all',
        'sonarMetricsReliability': 'all',
        'sonarMetricsSecurity': 'all',
        'sonarMetricsTests': 'all',
        'sonarProjectKey': 'petclinic',
        'sonarProjectName': 'petclinic',
        'sonarProjectVersion': '2.2.0.BUILD-SNAPSHOT',
        'sonarTaskId': '',
        'sonarTimeout': '',
      ]
      subpluginKey = 'EC-SonarQube'
      subprocedure = 'Get Last SonarQube Metrics'
      taskType = 'PLUGIN'
    }
  }

  stage 'Quality Assurance', {
    colorCode = '#ff7f0e'
    pipelineName = 'pipeline_Base'
    task 'Deploy to QA', {
      command = 'echo "replace me"'
      taskType = 'COMMAND'
    }
  }

  stage 'Production', {
    colorCode = '#2ca02c'
    pipelineName = 'pipeline_Base'

    task 'Deploy to Production', {
      command = 'echo "replace me"'
      taskType = 'COMMAND'
    }
  }

  // Custom properties

  property 'ec_counters', {

    // Custom properties
    pipelineCounter = '1'
  }
}