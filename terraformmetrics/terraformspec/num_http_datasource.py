from terraformmetrics.terraform_metric import TerraformMetric


class NumHttp(TerraformMetric):
    """ This class measures the number of modules used
    """

    def count(self):
        """Return the number of modules used
        Returns
        -------
        int
            Number of modules used
        """

        num_http = 0

        if 'data' in self.tfparsed:
            for elem in self.tfparsed['data']:
                if 'http' in elem:
                    num_http += 1

        return num_http
