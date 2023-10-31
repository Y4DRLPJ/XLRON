from absl import flags

# N.B. Use can pass the flag --flagfile=PATH_TO_FLAGFILE to add flags without typing them out

# Training hyperparameters
flags.DEFINE_float("LR", 5e-4, "Learning rate")
flags.DEFINE_integer("NUM_ENVS", 1, "Number of environments")
flags.DEFINE_integer("NUM_STEPS", 150, "Number of steps per environment")
flags.DEFINE_float("TOTAL_TIMESTEPS", 1e6, "Total number of timesteps")
flags.DEFINE_integer("UPDATE_EPOCHS", 10, "Number of epochs per update")
flags.DEFINE_integer("NUM_MINIBATCHES", 1, "Number of minibatches per update")
flags.DEFINE_float("GAMMA", 0.99, "Discount factor")
flags.DEFINE_float("GAE_LAMBDA", 0.95, "GAE lambda parameter")
flags.DEFINE_float("CLIP_EPS", 0.2, "PPO clipping parameter")
flags.DEFINE_float("ENT_COEF", 0.0, "Entropy coefficient")
flags.DEFINE_float("VF_COEF", 0.5, "Value function coefficient")
flags.DEFINE_float("MAX_GRAD_NORM", 0.5, "Maximum gradient norm")
flags.DEFINE_string("ACTIVATION", "tanh", "Activation function")
flags.DEFINE_string("LR_SCHEDULE", "warmup_cosine", "Learning rate schedule")
flags.DEFINE_integer("SCHEDULE_MULTIPLIER", 1, "Increase the learning rate schedule horizon "
                                               "by this factor (to keep schedule for longer final training runs "
                                               "consistent with that from tuning runs)")
flags.DEFINE_float("WARMUP_PEAK_MULTIPLIER", 1, "Increase the learning rate warmup peak compared to init")
flags.DEFINE_float("WARMUP_STEPS_FRACTION", 0.2, "Fraction of total timesteps to use for warmup")
flags.DEFINE_float("WARMUP_END_FRACTION", 0.1, "Fraction of init LR that is final LR")
flags.DEFINE_integer("SEED", 42, "Random seed")
flags.DEFINE_integer("NUM_SEEDS", 1, "Number of seeds")
flags.DEFINE_integer("NUM_LAYERS", 2, "Number of layers in actor and critic networks")
flags.DEFINE_integer("NUM_UNITS", 64, "Number of hidden units in actor and critic networks")
# Additional training parameters
flags.DEFINE_string("VISIBLE_DEVICES", "0", "Comma-separated indices of (desired) visible GPUs e.g. 1,2,3")
flags.DEFINE_boolean("PREALLOCATE_MEM", True, "Preallocate GPU memory")
flags.DEFINE_string("PREALLOCATE_MEM_FRACTION", "0.95", "Fraction of GPU memory to preallocate")
flags.DEFINE_boolean("PRINT_MEMORY_USE", False, "Print memory usage")
flags.DEFINE_boolean("USE_PMAP", False, "Use pmap")
flags.DEFINE_boolean("WANDB", False, "Use wandb")
flags.DEFINE_boolean("SAVE_MODEL", False, "Save model")
flags.DEFINE_boolean("DEBUG", False, "Debug mode")
flags.DEFINE_boolean("DEBUG_NANS", False, "Debug NaNs")
flags.DEFINE_boolean("ORDERED", True, "Order print statements when debugging "
                                      "(must be false if using pmap)")
flags.DEFINE_string("MODEL_PATH", ".", "Path to save/load model")
flags.DEFINE_string("PROJECT", "", "Name of project")
flags.DEFINE_string("EXPERIMENT_NAME", "", "Name of experiment")
flags.DEFINE_integer("DOWNSAMPLE_FACTOR", 1, "Downsample factor to reduce data uploaded to wandb")
flags.DEFINE_boolean("DISABLE_JIT", False, "Disable JIT compilation")
flags.DEFINE_boolean("ENABLE_X64", False, "Enable x64 floating point precision")
flags.DEFINE_boolean("ACTION_MASKING", False, "Use invalid action masking")
# Environment parameters
flags.DEFINE_string("env_type", "vone", "Environment type")
flags.DEFINE_integer("load", 150, "Load")
flags.DEFINE_integer("mean_service_holding_time", 15, "Mean service holding time")
flags.DEFINE_integer("k", 5, "Number of paths")
flags.DEFINE_string("topology_name", "4node", "Topology name")
flags.DEFINE_integer("link_resources", 5, "Number of link resources")
flags.DEFINE_float("max_requests", 4, "Maximum number of requests in an episode")
flags.DEFINE_float("max_timesteps", 30, "Maximum number of timesteps in an episode")
flags.DEFINE_integer("min_bw", 25, "Minimum requested bandwidth")
flags.DEFINE_integer("max_bw", 100, "Maximum requested bandwidth")
flags.DEFINE_integer("step_bw", 1, "Step size for requested bandwidth values between min and max")
flags.DEFINE_list("values_bw", None, "List of requested bandwidth values")
flags.DEFINE_float("slot_size", 12.5, "Spectral width of frequency slot in GHz")
flags.DEFINE_boolean("incremental_loading", False, "Incremental increase in traffic load until first blocking")
flags.DEFINE_boolean("continuous_operation", False, "If True, do not reset the environment at the end of an episode")
# RSA-specific environment parameters
flags.DEFINE_boolean("random_traffic", False, "Random traffic matrix for RSA on each reset (else uniform or custom)")
flags.DEFINE_string("custom_traffic_matrix_csv_filepath", None, "Path to custom traffic matrix CSV file")
# VONE-specific environment parameters
flags.DEFINE_integer("node_resources", 4, "Number of node resources")
flags.DEFINE_list("virtual_topologies", "3_ring", "Virtual topologies")
flags.DEFINE_integer("min_node_resources", 1, "Minimum number of node resources")
flags.DEFINE_integer("max_node_resources", 1, "Maximum number of node resources")
flags.DEFINE_list("node_probs", None, "List of node probabilities for selection")
# Heuristic-specific parameters
flags.DEFINE_boolean("EVAL_HEURISTIC", False, "Evaluate heuristic")
flags.DEFINE_string("path_heuristic", "ksp_ff", "Path heuristic to be evaluated")
flags.DEFINE_string("node_heuristic", "random", "Node heuristic to be evaluated")

