# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest


class ComputeRecommenderScenario(ScenarioTest):
    def test_spot_placement_recommender_generate(self):        
        self.kwargs.update({
            'location': 'eastus',
            'subscription_id': self.get_subscription_id(),
            'availability_zones': 'true',
            'desired_locations': '["eastus", "eastus2"]',
            'desired_count': 1,
            'desired_sizes': '[{"sku": "Standard_D2_v2"}]'
        })

        spot_scores_output = self.cmd('az compute-recommender spot-placement-recommender -l {location} --subscription {subscription_id} --availability-zones {availability_zones} --desired-locations \'{desired_locations}\' --desired-count {desired_count} --desired-sizes \'{desired_sizes}\'').get_output_in_json()

        self.assertTrue(len(spot_scores_output["placementScores"]) > 0, "Spot scores should have at least one item")