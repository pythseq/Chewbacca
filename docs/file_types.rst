File Types
==========
Chewbacca uses several common file types and a couple of unique ones. Those are described below.

Fasta File
-----------
**common extensions: .fa, .fasta, .FASTA**

Read more here: https://en.wikipedia.org/wiki/FASTA_format

FastQ File
-----------
**extensions: .fq, .fastq, .FASTQ**

Read more here: https://en.wikipedia.org/wiki/FASTQ_format

Groups File
------------
**Common Extensions: .groups**

Groups files are used by Chewbacca to keep track of groups, or clusters, of relatively similar sequences.
Group files are generated or updated after each dereplication or clustering step.
A Groups file consists of one or more lines in the following format:

  *GROUPID <tab> SequenceID (<space> SequenceID)* ...

As an example:

::

   Honolulu_site1_0_ID111     Honolulu_site1_0_ID111 Honolulu_site1_0_ID112 Honolulu_site1_0_ID113
   Indonedia_site1_0_ID115    Indonedia_site1_0_ID115 Indonedia_site1_0_ID117
   Philippines_site1_0_ID1    Philippines_site1_0_ID1 Philippines_site1_0_ID2


**Notes:**

1. The GROUPID for a group/cluster is a representative sequence from that cluster. This means that a sequenceId  will likely appear twice on a line (once as a GROUPID, and once in the sequence SequenceIds list).

2. See the "naming conventions" section for more info on chewbacca sequence naming standards. SequenceId are created using the a combination of sameple name, file offset,and the sequential number
   ex. Honolulu_site1_0_ID119.
   - Hawaii_site1: This sequence is from the Hawaii_site1 sample.
   - 0 file offset. When more than one sequence file is used, the files are annotated using different offesets. This makes it easy to track which sequences came from which file, which could potentially represent different sequencing runs, or other things of interest.

Samples File
-------------
**Common Extensions: .samples**


Samples files are used by Chewbacca to map sequence names to the the name of their respective sample names.
This file is generally written once, early on in the anylitical process, at the time of sequence renaming.
The primary purposes for writing this file are for annotation and construction of an OTU table at the end of the analysis.

A Samples file consists of one or more lines in the following format:
 
CC*SequenceID <tab> SampleID*

**Example**

::

   Hawaii_site1_0_ID111 GUT_SAMPLE_21
   Hawaii_site1_0_ID112 GUT_SAMPLE_21
   Rodent_gutID113 GUT_SAMPLE_22
   Rodent_noseID115     NOSE_SAMPLE_1
   Rodent_stomachID115  STOMACH_SAMPLE_2

Note that more than one sample file is generated when sequences form asample are present in more than one files. In such case,
Each file is assigned the a different offet. Ex.: Rodent_gut_0.samples, Rodent_gut_1.samples, etc...


Barcodes file
--------------
**Common Extensions: .barcodes, .txt**

Barcodes files map the nucleotide prefixes used for multiplexing, to the samples they code for.  

A Samples file consists of one or more lines in the following format:



	<Sample_name> <tab> <barcode_sequence>

**Example**

::

   BALI_site_1          agacgc
   BALI_site_2          agtgta
   Hawaii_site_1        actagc
   
Adapters file
--------------
**Common Extensions: .adapters, .txt, .fa, .fasta**

Adapters files are fasta files that contain the sequencing adapters.
An Adapters file should be paired with an RC Adapters file, and should contain the same number of entries as its paired RC Adapters file.

**Example**

::

   >adapter1
   GGWACWGGWTGAACWGTWTAYCCYCC
   >adapter2
   TANACYTCNGGRTGNCCRAARAAYCA


RC Adapters file
-----------------
**Common Extensions: .adapters, .txt, .fa, .fasta**

RC Adapters files are fasta files that contain the Reverse-read adapters (Reverse-Complemented forward-read adapters) pyrosequencing adapters.
An RC Adapters file should be paired with an Adapters file, and should contain the same number of entries as its paired Adapters file.

**Example**

::

   >adapter1_RC
   TGRTTYTTYGGNCAYCCNGARGTNTA
   >adapter2_RC
   GGRGGRTAWACWGTTCAWCCWGTWCC

Tax file
---------
**Common Extensions: .tax, .out, .txt**

Tax files are condensed versions of `blast6
<http://www.drive5.com/usearch/manual/blast6out.html>`_ output files,
detailing the match between a query sequence and a possible
identification. These files are generated by the :ref`id_OTU` command,
and ingested by the :ref`annotate_OTU` command.

Given the blast6 output format, a Tax file consists of one or more
lines in the following format:

::

   <query> <tab> <target> <tab> <id> <tab> <alnlen> <tab> <qcov>

**Example**

::

   BALI4606_0_ID1264_2	GBMAA1117-14	90.6	265	84.7	Animalia;Porifera;Demospongiae;Haplosclerida;Phloeodictyidae;;Calyx;Calyx podatypa
   BALI4462_0_ID921_1	GBCI5234-15	98.8	258	82.4	Animalia;Cnidaria;Anthozoa;Alcyonacea;Xeniidae;;Xenia;Xenia sp. 1 CSM2014
   BALI4673_0_ID837_1	KHA237-14	96.1	279	100.0	Animalia;Cnidaria;Anthozoa;Actiniaria;;;;

OTU Table
---------
**Common Extensions: .txt**

OTU tables are commonly used in Biological surveys to list OTU abundances in different samples.  

OTU tables consist of a header line in the following format:

::

   OTU <tab> <Samplename1> <tab> <Samplename2> <tab> <Samplename3> ...

followed by one or more lines (one per OTU) in the follwing format:

::

   <OTU_name> <tab> <Abundance at Samplename1> <tab> <Abundance at Samplename2> <tab> <Abundance at Samplename3>

**Example**

::

   OTU	Hawaii_site1	Indonesia_site2	...
   Rat_Gut_ID3	3	0	...
   Rat_Gut_ID25	1	1	...
   
Mapping file
------------
**Common Extensions: .mapping, .txt**

Mapping files are artifacts of renaming (via the :ref:`rename`
command), and map old sequence ids to new sequence ids.  This allows
users to use shorter and meaningful sequence ids, while still having
access to the original sequence names.

A Mapping file consists of one or more lines in the following format:

::

   <old_sequence_name> <tab> <new_sequence_name>

**Example**

::

   M03292:26:000000000-AH6AG:1:1101:16896:1196	BALI4462_0_ID1
   M03292:26:000000000-AH6AG:1:1101:12506:1361	BALI4462_0_ID2
   M03292:26:000000000-AH6AG:1:1101:15278:1402	BALI4462_0_ID3
   M03292:26:000000000-AH6AG:1:1101:16930:1429	BALI4462_0_ID4
