#General Metrics
from terraformmetrics.general.lines_code import LinesCode
from terraformmetrics.general.lines_blank import LinesBlank
from terraformmetrics.general.lines_comment import LinesComment
from terraformmetrics.general.num_conditions import NumConditions
from terraformmetrics.general.num_decisions import NumDecisions

#Terraform specific
from terraformmetrics.terraformspec.num_resources import NumResources
from terraformmetrics.terraformspec.avg_resource_size import AvgResourcesSize
from terraformmetrics.terraformspec.num_remote_exec import NumRemoteExec

general_metrics = {
                    'lines_code': LinesCode,
                    'lines_blank': LinesBlank,
                    'lines_comment': LinesComment,
                    'num_conditions': NumConditions,
                    'num_decisions': NumDecisions,
                  }
tf_metrics = {
                'num_resources': NumResources,
                'avg_resources_size': AvgResourcesSize,
                'num_remote_exec': NumRemoteExec,
             }

