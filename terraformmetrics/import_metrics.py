#DA FAREtutti gli import
from terraformmetrics.general.lines_code import LinesCode
from terraformmetrics.general.lines_blank import LinesBlank
from terraformmetrics.general.lines_comment import LinesComment
from terraformmetrics.general.num_conditions import NumConditions
from terraformmetrics.general.num_decisions import NumDecisions

general_metrics = {
                    'lines_code': LinesCode,
                    'lines_blank': LinesBlank,
                    'lines_comment': LinesComment,
                    'num_conditions': NumConditions,
                    'num_decisions': NumDecisions,
                  }
tf_metrics = {}

