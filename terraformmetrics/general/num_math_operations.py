from terraformmetrics.terraform_metric import TerraformMetric

import re


class NumMath(TerraformMetric):
    """ The try function is used for error handling, the method counts the number of occurrences of the latter
    """

    def count(self):
        """Return the number of try functions
        Returns
        -------
        int
            Number of try functions
        """

        # Funzione ricorsiva per contare il numero di funzioni try
        def count_operators(expression):
            if isinstance(expression, list):
                count = 0
                for item in expression:
                    count += count_operators(item)
                return count
            elif isinstance(expression, dict):
                count = 0
                for key, value in expression.items():
                    if isinstance(value, str):
                        operators = [' + ', ' - ', ' * ', ' / ', ' % ', ' ^ ']
                        count += sum(1 for operator in operators if operator in value)
                    count += count_operators(value)
                return count
            else:
                return 0

        total_try_count = count_operators(self.tfparsed)

        return total_try_count