# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kaspar/DAT113/exercises/exam

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kaspar/DAT113/exercises/exam/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/exam.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/exam.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/exam.dir/flags.make

CMakeFiles/exam.dir/main.c.o: CMakeFiles/exam.dir/flags.make
CMakeFiles/exam.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kaspar/DAT113/exercises/exam/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/exam.dir/main.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/exam.dir/main.c.o   -c /Users/kaspar/DAT113/exercises/exam/main.c

CMakeFiles/exam.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/exam.dir/main.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kaspar/DAT113/exercises/exam/main.c > CMakeFiles/exam.dir/main.c.i

CMakeFiles/exam.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/exam.dir/main.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kaspar/DAT113/exercises/exam/main.c -o CMakeFiles/exam.dir/main.c.s

CMakeFiles/exam.dir/main.c.o.requires:

.PHONY : CMakeFiles/exam.dir/main.c.o.requires

CMakeFiles/exam.dir/main.c.o.provides: CMakeFiles/exam.dir/main.c.o.requires
	$(MAKE) -f CMakeFiles/exam.dir/build.make CMakeFiles/exam.dir/main.c.o.provides.build
.PHONY : CMakeFiles/exam.dir/main.c.o.provides

CMakeFiles/exam.dir/main.c.o.provides.build: CMakeFiles/exam.dir/main.c.o


# Object files for target exam
exam_OBJECTS = \
"CMakeFiles/exam.dir/main.c.o"

# External object files for target exam
exam_EXTERNAL_OBJECTS =

exam: CMakeFiles/exam.dir/main.c.o
exam: CMakeFiles/exam.dir/build.make
exam: CMakeFiles/exam.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kaspar/DAT113/exercises/exam/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable exam"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/exam.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/exam.dir/build: exam

.PHONY : CMakeFiles/exam.dir/build

CMakeFiles/exam.dir/requires: CMakeFiles/exam.dir/main.c.o.requires

.PHONY : CMakeFiles/exam.dir/requires

CMakeFiles/exam.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/exam.dir/cmake_clean.cmake
.PHONY : CMakeFiles/exam.dir/clean

CMakeFiles/exam.dir/depend:
	cd /Users/kaspar/DAT113/exercises/exam/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kaspar/DAT113/exercises/exam /Users/kaspar/DAT113/exercises/exam /Users/kaspar/DAT113/exercises/exam/cmake-build-debug /Users/kaspar/DAT113/exercises/exam/cmake-build-debug /Users/kaspar/DAT113/exercises/exam/cmake-build-debug/CMakeFiles/exam.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/exam.dir/depend
