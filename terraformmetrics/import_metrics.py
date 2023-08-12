#General Metrics
from terraformmetrics.general.lines_code import LinesCode
from terraformmetrics.general.lines_blank import LinesBlank
from terraformmetrics.general.lines_comment import LinesComment
from terraformmetrics.general.num_conditions import NumConditions
from terraformmetrics.general.num_decisions import NumDecisions
from terraformmetrics.general.num_tokens import NumTokens

#Terraform specific
from terraformmetrics.terraformspec.num_resources import NumResources
from terraformmetrics.terraformspec.avg_resource_size import AvgResourcesSize
from terraformmetrics.terraformspec.num_remote_exec import NumRemoteExec
from terraformmetrics.terraformspec.num_file_provisioner import NumFileProvisioner
from terraformmetrics.terraformspec.num_permissions import NumFilePermissions
from terraformmetrics.terraformspec.num_modules import NumModules
from terraformmetrics.terraformspec.num_http_datasource import NumHttp
from terraformmetrics.terraformspec.num_error_handling import NumErrorHandling

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
                'num_remote_exec_provisioner': NumRemoteExec,
                'num_file_provisioner': NumFileProvisioner,
                'num_permissions': NumFilePermissions,
                'num_modules': NumModules,
                'num_http_datasource': NumHttp,
                'num_error_handling': NumErrorHandling,
                'num_tokens': NumTokens,
             }

