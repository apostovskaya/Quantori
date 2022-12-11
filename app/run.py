python3 script.py "ATTTGGCTACTAACAATCTA"
python3 script.py "ATTTGGCTACTAACAATCTA" "transform"
python3 script.py "ATTTGGCTACTAACAATCTA" "transcription"

# config
# main directory = main folder of the project (Quantori)
dir_main = ".."
# APP_DIR

# credentials for Postgres DB
# db_user = "postgres"
# db_pswrd = "secretpassword"
# db_host = "db"
# db_port = "5432"
# db_name = "molbiol_central_dogma"

# DB_URI
# db_info = f"postgresql://{db_user}:{db_pswrd}@{db_host}:{db_port}/{db_name}"

# db build
# Base = declarative_base()

# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('postgresql+psycopg2://postgres:password@db:5432/project')
# engine = create_engine('postgresql+psycopg2://user:password@localhost:5432'
#                        '/molbiol_central_dogma.db',
#                        echo=True, pool_pre_ping=True)

# engine = create_engine('sqlite:///test.db', echo=True)
# molbiol_central_dogma

# Base = declarative_base()

# "localhost" (127.0.0.1)


# db design
# from sqlalchemy.ext.declarative import declarative_base


# script
# plot with default params: bin size of 100, .png format
# smaller_genome = genome[:5000]
# plot_gc_content(smaller_genome)
#
# # plot with provided params
# plot_gc_content(genome, 50000, '.JPEG')

python3 ./app/script.py "ATTTGGCTACTAACAATCTA" "transcription" 50000