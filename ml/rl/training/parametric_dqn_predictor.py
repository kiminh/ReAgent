#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

import logging

from ml.rl.training.sandboxed_predictor import SandboxedRLPredictor


logger = logging.getLogger(__name__)


class ParametricDQNPredictor(SandboxedRLPredictor):
    def predict(self, float_state_features, actions):

        float_examples = []
        for i in range(len(float_state_features)):
            float_examples.append({**float_state_features[i], **actions[i]})

        return super().predict(float_examples)
