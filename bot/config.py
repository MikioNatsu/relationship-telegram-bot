import os

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    DATABASE_PATH = os.getenv('DATABASE_PATH')
    SPARK_DAILY_CAP = int(os.getenv('SPARK_DAILY_CAP', 100))
    RELATIONSHIP_LEVELS = os.getenv('RELATIONSHIP_LEVELS', 'none,low,medium,high').split(',')
    ACTION_CATEGORIES = os.getenv('ACTION_CATEGORIES', 'default').split(',')
    RESPONSE_MODES = os.getenv('RESPONSE_MODES', 'text,image,video').split(',')
    COOLDOWN_SECONDS = int(os.getenv('COOLDOWN_SECONDS', 60))
    PROPOSAL_EXPIRY_MINUTES = int(os.getenv('PROPOSAL_EXPIRY_MINUTES', 30))
    SPARK_DECAY_FACTOR = float(os.getenv('SPARK_DECAY_FACTOR', 0.5))
    ACTION_LOG_RETENTION_DAYS = int(os.getenv('ACTION_LOG_RETENTION_DAYS', 7))
