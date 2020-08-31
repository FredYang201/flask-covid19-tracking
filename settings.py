class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:604030@127.0.0.1:3306/covid'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://rpgwzdkugnuewy:59747d223eb59b4c7c339919c00fbce21bdfae9f7dd2c9d7ea2fac523a51c774@ec2-54-144-177-189.compute-1.amazonaws.com:5432/d4od1eo3ga2i2c'