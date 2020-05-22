create table users (
    id integer primary key autoincrement,
    name text not null,
    password text not null,
    admin boolean not null
);

create table questions (
    id integer primary key autoincrement,
    quiz_name text not null,
    question_text text not null,
    answer text not null,
);