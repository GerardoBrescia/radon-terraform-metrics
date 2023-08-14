from terraformmetrics.terraform_metric import TerraformMetric


class NumDynamicBlock(TerraformMetric):
    """ This class measures the number of input vars in a Script Terraform
    """

    def count(self):
        """Return the number of input vars
        Returns
        -------
        int
            Number of input vars
        """

        # Funzione ricorsiva per contare il numero di variabili all'interno di un file
        def count_dynamic_blocks(data):
            count = 0

            if isinstance(data, dict):
                for key, value in data.items():
                    if key == "dynamic":
                        count += len(value)
                    else:
                        count += count_dynamic_blocks(value)
            elif isinstance(data, list):
                for item in data:
                    count += count_dynamic_blocks(item)

            return count

        total_dynamic_count = count_dynamic_blocks(self.tfparsed)

        return total_dynamic_count
