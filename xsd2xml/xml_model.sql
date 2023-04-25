create table Element (
    id integer primary key,
    element_name text,
    namespace_id integer,
    parent_id integer,
    foreign key (namespace_id) references Namespace(id),
    foreign key (parent_id) references Element(id)
);

create table Attribute (
    id integer primary key,
    attr_name text,
    attr_value text,
    element_id integer,
    foreign key (element_id) references Element(id)
);

create table Text (
    id integer primary key,
    content text,
    element_id,
    foreign key (element_id) references Element(id)
);

create table Namespace (
    id integer primary key,
    prefix_name text,
    url text
);
