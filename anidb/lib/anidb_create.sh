db=anidb.db
touch $db

exec_sql()
{
  sqlite3 --batch $db "$*"
}

sql_create="
CREATE TABLE titles (
  aid TEXT,
  type TEXT,
  language TEXT,
  title TEXT
);
"

exec_sql "$sql_create"
