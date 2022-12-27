# File System Program

## Favour Ojo

## Overview of the Completed Project in At Least Two Paragraphs

For this project, I implemented a File System Program that allows
an user to create a directory, add a file to that specified directory,
and also show details about that specified file. Within this project, I
have been able to create functions that are able to replicate actions
that are done by individuals in the file explorer. Though the file explorer
varies between the 3 main, also different, operating systems, MacOS, Windows,
and Linux, all the actions within a file explorer are very similar. However,
since my operating system is a Windows machine, I replicated the Windows version
of a file explorer.

## Example of Output Demonstrating that your Project Works Correctly

```python

Welcome to the File System Program!
-------------------------------------

Content of the File System Program will be in the pyremove.py program

First, lets create the directory:
Directory created!

You have successfully created the directory

Now, lets add a file into the directory:

Here are the file contents:

You have successfully added the file!

Now, we are going to display the attributes of the file
names.csv

Size: 158 bytes

Last accessed: Thu Dec  8 13:02:10 2022
Last Modified: 08 Dec 2022

You can display the read, write, and execute permissions of the file!
Read permission: True
Write permission: True
Execute permission: False
```

In this output, you can see how the program operates when there is not already
a directory and file created. Once you have run the command `python pyremove.py`,
the program with first introduce you to the file system program. After doing that,
it will then say the content of the file system program is located in the `pyremove.py`
program. This action was doing using the command line implementation to display the 
name of the program that is being run. After this, the `create_dir()` function is called and 
a directory is then created in the same location where the `pyremove.py` is located. Once the
directory, it is now time to add the file to the directory. The way to add a file to the directory
you have created is by calling the `create_file()` function, and the program will print out a succesful
message if you have called the function correctly.  After successfully adding the file, the program
will then start to display the attrivutes of the file and the program will display the name of the file.
The program will then display the size of the file, when the file was last accessed and when it was last
modified. After doiing that, the program will finally display if the file has read, write, and execute permissions
utilizing the `boolean` factor.


```python
Welcome to the File System Program!
-------------------------------------

Content of the File System Program will be in the pyremove.py program

First, lets create the directory:
Directory already exists!

You have successfully created the directory

Now, lets add a file into the directory:

Here are the file contents:
Sarah Wilcox

Courtney Torres

Teresa Cabrera

Michael Dunn

Gary Larson

Tracey Hopkins

Erica Thompson

Mary Houston

Greg Scott

Maria Mccarthy


You have successfully added the file!

Now, we are going to display the attributes of the file
names.csv

Size: 336 bytes

Last accessed: Thu Dec  8 13:02:36 2022
Last Modified: 08 Dec 2022

You can display the read, write, and execute permissions of the file!
Read permission: True
Write permission: True
Execute permission: False
```

Similar to the above output, you are also attempting to create a directory and file.
However, with this output, it is showing what happens whenever a directory or file is
already present in the file explorer. Once you have run the command `python pyremove.py`,
the program with first introduce you to the file system program, just like the above output. After doing that,
it will then say the content of the file system program is located in the `pyremove.py`
program. This action was done using the command line implementation to display the 
name of the program that is being run. After this, the `create_dir()` function is called and 
the program will state that a directory has already been created and you have already created the directory.
Once you call the `create_file()` function, the program will now output the contents of the file to show 
that the file has already been created and there is content inside it. Similar to the above output, the 
program will display the attributes of the file that has been created. 

## Overview of Some Source Code that is Central to your Project

```python
def create_dir():
    """Creates a directory that will include the file"""
    outdir = Path.cwd() / "data"
    if Path.exists(outdir) == True:
        print("Directory already exists!")
    else:
        outdir.mkdir(parents=True, exist_ok=True)
        print("Directory created!")

    return outdir
```

In the `create_dir()` function, you are creating a directory within the
same location where the `pyremove.py` program is location. First, by utilizing
the `Pathlib` module in the Python programming language, we are creating the path
for the directory `data`. The path of the directory is assigned to the variable
`outdir`. Once the path of the `data` directory, I then implemented conditional
logic to indicate that if the directory already exists then the program should
output the phrase "Directory already exists". If the directory does not exist,
that the variable `outdir` utilizes the `mkdir` implementation to make the directory
and output that the directory has been created. After doing that, the function will
then return the value of the variable `outdir`. 

```python
def create_file():
    """Generates fake names to CSV file"""
    # creating Faker module
    fake = Faker()
    fake.name()
    
    # writing into files
    with open(N_PATH, 'a') as csvfile:
        filewriter = csv.writer(csvfile)
        for i in range(10):
            filewriter.writerow([fake.name()])

        myFile = open(N_PATH, "r")
        print(myFile.read())
        myFile.close()
```

In the `create_file()` function, we are creating a file in the directory while also
generating fake names to the CSV file. First, you would need to create the Faker
module to create the names that will be generated to the CSV file. You would need
to called the Faker module with fake names like so, `fake.name`. Then, the user
would then need to write into the files so the names can be listed in there. This
is done using the `with open` implemented to open the file path as a csv file. After
doing that we utilized the `csv` module to write inside the file . After doing this, 
we then print out the file contents utilizing the `read` implementation. 

## Description of How Your Project Connects to a Key Operating Systems Concept

The project I have created for my long systems project relates to the concept
of File Systems and Directories. I have been able to utilize `os` module to 
be able to manipulate files that I have been able to create and directories
that I have also been able to create. While completing this project, I have
been able to enhance my knowledge on how files and directories operate in a
Windows operating system.

## Description of Resources that You Consulted to Complete the Project

I was able to utilize several resources online that realted to the topic
of my project. I was able to see the different ways individuals have been
able to work with file paths, directories, and files. Since I am operating
on a Windows machine, I would have to specify how to complete certain operations
with a Windows machine. I especially had to do this when looking at how to write
a file path in Python. This is because file paths vary between each operating system
Linux, MacOS, and Windows.

## Statement of Future Work you Could Conduct Using Your System as a Baseline

For the future work of this project, I would primarily work on trying to add multiple
files at a time to the directory that has been created. As of right now, the project
can only create one singular file to the directory `data`. I believe if I am to create
multiple files into the directory, it would replicate a more accurate version of the
file explorer that is available in all 3 operating system, MacOS, Windows, and Linux.
