# sqLite-Lec6-Jan-08-25
SQL 1-N, N-N
* N-N:
  * theory:
    *   usually will be in a separate table that contain the PK of 1st table and PK of 2nd table:
      * there are 2 ways to do it: 
        * a table with 1 PK made from the 2 PK from the 2 tables 
          * these PKs are FKs references to the 1st and 2nd tables
        * a table with separated PK AI and 2 other Unique FKs of the PK from the other tables

