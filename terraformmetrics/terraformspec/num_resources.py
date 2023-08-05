from terraformmetrics.terraform_metric import TerraformMetric

class NumResources(TerraformMetric):
    """ This class measures the number of decisions within an if block in a Script Terraform

    decisions are identified by counting the number of occurrences of the operators : (&& || !)
    within an if block
    """

    def count(self):
        """Return the number of conditions
        Returns
        -------
        int
            Number of conditions
        """
        resource_list = self.tffile.get('resource', [])
        resource = len(resource_list)

        return resource



