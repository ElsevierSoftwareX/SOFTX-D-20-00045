<div style="width:150px; height:100px">
![openTEPES](doc/img/openTEPES_img.png)
</div>
**Open Generation and Transmission Operation and Expansion Planning Model with RES and ESS (openTEPES)**

*Simplicity and Transparency in Power Systems Planning*

The openTEPES model has been developed at the [Instituto de Investigación Tecnológica (IIT)](https://www.iit.comillas.edu/index.php.en) of the [Universidad Pontificia Comillas](https://www.comillas.edu/en/).

**openTEPES** determines the investment plans of new facilities (generators, ESS and lines) for supplying the forecasted demand at minimum cost. Tactical planning is concerned with time horizons of 10-20 years. Its objective is to evaluate the future generation, storage and network needs. The main results are the guidelines for the future structure of the generation and transmission systems.

In addition, the model presents a decision support system for defining the generation and transmission expansion plan of a large-scale electric system at a tactical level, defined as a set of generation and network investment decisions for future years. The expansion candidate, generators, ESS and lines, are pre-defined by the user, so the model determines the optimal decisions among those specified by the user.

It determines automatically optimal expansion plans that satisfy simultaneously several attributes. Its main characteristics are:

1. **Static:** the scope of the model corresponds to a single year at a long-term horizon, 2030 or 2040 for example.
   It represents hierarchically the different time scopes to take decisions in an electric system:

    1. Period: one year

    2. Load level: 2030-01-01T00:00:00+01:00 to 2030-12-30T23:00:00+01:00

    The time division allows a flexible representation of the periods for evaluating the system operation. For example, by a set of non-chronological isolated snapshots or by 2920 periods of three hours or by the 8760 hours of the year.

2. **Stochastic:** several stochastic parameters that can influence the optimal generation and transmission expansion decisions are considered. The model considers stochastic short-term yearly uncertainties (scenarios) related to the system operation. The operation scenarios are associated with renewable energy sources and electricity demand.

Multicriteria: the objective function incorporates some of the main quantifiable objectives: **generation and transmission investment cost (CAPEX)** and **expected variable operation costs (including generation emission cost) (system OPEX)**.

The model formulates an optimization problem including generation and network binary investment decisions and operation decisions.

The operation model is a **network constrained unit commitment (NCUC)** based on a **tight and compact** formulation including operating reserves with a **DC power flow (DCPF)**. Network ohmic losses are considered proportional to the line flow. It considers different **energy storage systems (ESS)**, e.g., pumped-storage hydro, battery, etc. It allows analyzing the trade-off between the investment in generation/transmission and the use of storage capacity.

The main results of the model can be structured in these topics:

- **Investment:** investment decisions and cost

- **Operation:** the output of different units and technologies (thermal, storage hydro, pumped-storage hydro, RES), RES curtailment, line flows, line ohmic losses, node voltage angles

- **Emissions:** CO2

- **Marginal:** Locational Short-Run Marginal Costs (LSRMC)

A careful implementation has been done to avoid numerical problems by scaling parameters, variables and equations of the optimization problem allowing the model to be used for large-scale cases.

## Installation

There are 2 ways to get all required packages under Windows. We recommend using the Python distribution Anaconda. If you don't want to use it or already have an existing Python (version 3.8 **recommended**, 2.7 is supported as well) installation, you can also download the required packages by yourself.

### Anaconda/Miniconda (recommended)

  1. **[Anaconda (Python 3)](https://www.anaconda.com/products/individual)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html)**. Choose the 64-bit installer if possible.
     During the installation procedure, keep both checkboxes "modify the PATH" and "register Python" selected! If only higher Python versions are available, you can switch to a specific Python Version by typing `conda install python=<version>`
     1. **Remark:** if Anaconda or Miniconda was installed previously, please check that python is registered in the environment variables.
  2. **Packages and Solver**:
     1. Launch a new command prompt (Windows: Win+R, type "cmd", Enter)
     2. Install [GLPK](http://winglpk.sourceforge.net/) and [Cartopy](https://pypi.org/project/Cartopy/) via conda by `conda install glpk cartopy`
     3. Install openTEPES via pip by `pip install openTEPES`

Continue at [Get Started](#get-started).

### GitHub Repository (the hard way)
1. Clone the [openTEPES](https://github.com/IIT-EnergySystemModels/openTEPES/tree/master) repository. 
2. Launch the command prompt (Windows: Win+R, type "cmd", Enter), or the Anaconda prompt
3. Set up the path by `cd "C:\Users\<username>\...\openTEPES"`. (Note that the path is where the repository was cloned.)
4. Install openTEPES via pip by `pip install .`.
  
## Get started

### Developers
By cloning the [openTEPES](https://github.com/IIT-EnergySystemModels/openTEPES/tree/master) repository, you can create branches and propose pull-request. Any help will be very appreciated.

Continue like the users for a simple way of executions. 

### Users

If you are not planning on developing, please follows the instructions of the [Installation](#installation).

Once installation is complete, [openTEPES](https://github.com/IIT-EnergySystemModels/openTEPES/tree/master) can be executed in a test mode by using a command prompt. 
In the directory of your choice, open and execute the openTEPES_run.py script by using the following on the command prompt (Windows) or Terminal (Linux). (Depending on what your standard python version is, you might need to call `python3` instead of `python`.):
 
    openTEPES_run
Then, three parameters (case, dir, and solver) will be asked for.

**Remark:** at this step only press enter for each input and openTEPES will be executed with the default parameters.
   
After this in a directory of your choice, make a copy of the [9n](https://github.com/IIT-EnergySystemModels/openTEPES/tree/master/openTEPES/9n) or [sSEP](https://github.com/IIT-EnergySystemModels/openTEPES/tree/master/openTEPES/sSEP) case to create a new case of your choice but using the current format of the CSV files.
A proper execution by `openTEPES_run` can be made by introducing the new case and the directory of your choice. Note that the solver is `glpk` by default, but it can be changed by other solvers that pyomo supports.

Then, the `results` should be written in the folder whois called with the case name. The results contain plots and summary spreadsheets for multiple optimised energy scenarios, periods and load levels as well as the investment decisions.

## Tips

  1. A complete documentation of the openTEPES model can be found at https://pascua.iit.comillas.edu/aramos/openTEPES/index.html#, which presents the mathematical formulation, inputs and expected results. 
  2. Try adding/modifying the `TimeStep` in `oT_Data_Parameter_<case>.csv` and see their effect on results.
  3. Using `0` or `1`, the optimization options can be activated or deactivated in `oT_Data_Option_<case>.csv`.
  4. If you need a nice python editor, think about using [PyCharm](https://www.jetbrains.com/pycharm/download). It has many features including project management, etc.
  5. Creating a new script `script.py`, and write the following: 
      
    from openTEPES.openTEPES import execution
    execution(<case>, <dir>, <solver>)

## Screenshots
![center](doc/img/oT_Plot_MapNetwork_9n.png "Network map with investment decisions.")
![center](doc/img/oT_Plot_TechnologyOutput_sc01_y2030_9n.png "Power generation output by technology considering 8736 load levels for a year.")
