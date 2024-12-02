# Makefiles are files that automate the build process for C++
#-and other low-level languages like asm.

# Typically consists of a bunch of rules structured like:

# target: dependencies 
#	commands       

# target is the name of the file to generate, dependencies are files
#-needed to build the target, and commands are shell commands.

# variables:
CXX = g++                # C++ compiler
AS = as                  # assembler
CXXFLAGS = -O2                # C++ compiler flag for optimization
ASFLAGS = -arch arm64    # assembler flags that tell system type
LDFLAGS = -lm            # linking flags
SRC_DIR = src
BUILD_DIR = build

# source files
CPP_SRC = $(SRC_DIR)/cpp/main.cpp
ASM_SRC = $(SRC_DIR)/asm/math_operations.asm

# object files
CPP_OBJ = $(BUILD_DIR)/main.o
ASM_OBJ = $(BUILD_DIR)/math_operations.o

# Target executable
TARGET = $(BUILD_DIR)/calculator

# default rule that builds target executable
all: $(TARGET)

# building target
$(TARGET): $(CPP_OBJ) $(ASM_OBJ)
	$(CXX) $(CPP_OBJ) $(ASM_OBJ) -o $@ $(LDFLAGS)
# compiling c++
$(CPP_OBJ): $(CPP_SRC)
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@
# compiling asm
$(ASM_OBJ): $(ASM_SRC)
	mkdir -p $(BUILD_DIR)
	$(AS) $(ASFLAGS) $< -o $@
#clean build directory
clean:
	rm -rf $(BUILD_DIR)

# makes sure there's no name conflicts
.PHONY: all clean
