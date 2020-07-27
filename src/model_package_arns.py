class ModelPackageArnProvider:

    @staticmethod
    def get_model_package_arn(current_region):
        mapping = {
          "us-east-2" : "arn:aws:sagemaker:us-east-2:165536952993:model-package/facemask-1595876962"
        }
        return mapping[current_region]
