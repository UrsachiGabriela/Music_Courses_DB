INSERT INTO profesori(nume) VALUES ('Sandu Elena');
INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (profesori_id_profesor_seq.CURRVAL,4,30,0,'chitara',200);
INSERT INTO program VALUES ('luni',to_date('10:00 ','HH24:MI'),110,cursuri_id_curs_seq.CURRVAL);
INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (profesori_id_profesor_seq.CURRVAL,3,40,0,'pian',125);
INSERT INTO program VALUES ('marti',to_date('14:00 ','HH24:MI'),115,cursuri_id_curs_seq.CURRVAL);


INSERT INTO profesori(nume) VALUES ('Chiriac Alexandru');
INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (profesori_id_profesor_seq.CURRVAL,2,25,0,'orga',170);
INSERT INTO program VALUES ('marti',to_date('14:00 ','HH24:MI'),215,cursuri_id_curs_seq.CURRVAL);


INSERT INTO profesori(nume) VALUES ('Albu Ionel');
INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (profesori_id_profesor_seq.CURRVAL,4,15,0,'flaut',350);
INSERT INTO program VALUES ('joi',to_date('15:00 ','HH24:MI'),110,cursuri_id_curs_seq.CURRVAL);
INSERT INTO program VALUES ('vineri',to_date('11:00 ','HH24:MI'),110,cursuri_id_curs_seq.CURRVAL);


INSERT INTO profesori(nume) VALUES ('Simionescu Elena');
INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (profesori_id_profesor_seq.CURRVAL,3,25,0,'vioara',230);
INSERT INTO program VALUES ('miercuri',to_date('13:00 ','HH24:MI'),118,cursuri_id_curs_seq.CURRVAL);

INSERT INTO profesori(nume) VALUES ('Balan Maria');
INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (profesori_id_profesor_seq.CURRVAL,3,5,0,'harpa',230);
INSERT INTO program VALUES ('miercuri',to_date('15:00 ','HH24:MI'),118,cursuri_id_curs_seq.CURRVAL);





INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Popescu Ioana',22,'student');
INSERT INTO detalii_cursanti VALUES ('F','ipopescu@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('23-dec-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,6);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=6 ;
    
    
INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Moisescu Paula',17,'elev');
INSERT INTO detalii_cursanti VALUES ('F','mp@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('25-dec-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,6);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=6 ;
        
    
INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Toader Maria',21,'student');
INSERT INTO detalii_cursanti VALUES ('F','mtoader@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('18-dec-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,6);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=6 ;    
    
    
INSERT INTO cursanti(nume,varsta) VALUES ('Chirila Teodor',19);
INSERT INTO detalii_cursanti VALUES ('M','tchirila@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('20-dec-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,6);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=6 ;    
    

INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Andreescu Bianca',20,'student');
INSERT INTO detalii_cursanti VALUES ('F','b_and@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('02-jan-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,6);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=6 ;    
        
  
    
INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Andreescu Marius',16,'elev');
INSERT INTO detalii_cursanti VALUES ('M','ma@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('3-sep-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,1);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=1;
    
INSERT INTO cursanti(nume,varsta) VALUES ('Alecu Tatiana',21);
INSERT INTO detalii_cursanti VALUES ('F','tatiana_a@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('13-mar-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,3);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=3;
    
--cursant care doreste sa se inscrie la 2 cursuri
INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Georgescu Monica',17,'elev');
INSERT INTO detalii_cursanti VALUES ('F','g_monica@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('4-feb-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,4);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=4;
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('4-feb-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,1);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=1;
    
INSERT INTO cursanti(nume,varsta,ocupatie) VALUES ('Popovici Matei',19,'student');
INSERT INTO detalii_cursanti VALUES ('M','matei_p@gmail.com',cursanti_id_cursant_seq.CURRVAL);
INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date('6-oct-2021','dd-mon-yyyy'),cursanti_id_cursant_seq.CURRVAL,2);
UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=2;


--eliberare locuri curs ( atunci cand se finalizeaza perioada de invatare si se primeste o nota de evaluare a cunostintelor dobandite )
UPDATE fisa_inscriere SET nota_evaluare=8 WHERE id_cursant=2 AND id_curs=6;
UPDATE cursuri SET nr_inscrisi=nr_inscrisi-1 WHERE id_curs=6;

UPDATE fisa_inscriere SET nota_evaluare=10 WHERE id_cursant=9 AND id_curs=2;
UPDATE cursuri SET nr_inscrisi = nr_inscrisi-1 WHERE id_curs=2;


