from .cq_learner import CQLearner
from .facmac_learner import FACMACLearner
from .maddpg_learner import MADDPGLearner
from .rr_maddpg_learner import RRMADDPGLearner
from .rr_facmac_learner import RRFACMACLearner


REGISTRY = {}
REGISTRY["cq_learner"] = CQLearner
REGISTRY["facmac_learner"] = FACMACLearner
REGISTRY["maddpg_learner"] = MADDPGLearner
REGISTRY["rr_maddpg_learner"] = RRMADDPGLearner
REGISTRY["rr_facmac_learner"] = RRFACMACLearner

