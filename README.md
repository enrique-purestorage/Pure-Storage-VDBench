# Storage Performance Testing Tool

A comprehensive GUI-based tool for storage performance testing using VDBench, built with Streamlit and Python.

## Quick Start

1. **Prerequisites:**
   - Python 3.7+
   - VDBench (version 50406 or later)
   - Git (optional)

2. **Install VDBench:**
   - Download from: https://www.oracle.com/downloads/server-storage/vdbench-downloads.html
   - Follow VDBench installation steps in [Installation Guide](#installation--running)

3. **Install the Tool:**
   ```bash
   git clone https://github.com/enrique-purestorage/Pure-Storage-VDBench.git
   cd Pure-Storage-VDBench
   pip install -r requirements.txt
   ```

4. **Run the Tool:**
   ```bash
   streamlit run vdbench_ui.py
   ```

## Overview

This application provides a user-friendly interface for running storage performance tests and visualizing results in real-time. It leverages VDBench for the underlying testing while providing an intuitive web interface for configuration and monitoring.

## Legal Disclaimers

### 1. Software Provided "As Is"
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. The user assumes all responsibility and risk for the use of this software.

### 2. No Pure Storage Support
This tool is a community project and is NOT officially supported by Pure Storage. Pure Storage and its affiliates do not provide any maintenance, technical support, or updates for this software. Users should not contact Pure Storage support for assistance with this tool.

### 3. Limitation of Liability
IN NO EVENT SHALL PURE STORAGE, ITS AFFILIATES, OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### 4. No Affiliation Statement
While this tool may be used with Pure Storage products, it is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by Pure Storage. All product and company names are the registered trademarks of their original owners. Any use of Pure Storage product names is for reference purposes only and does not imply any official connection to or approval by Pure Storage.

## License

Copyright (c) 2024 Enrique Pure Storage. All rights reserved.

Permission is hereby granted, free of charge, to individuals and organizations, 
excluding direct competitors in the storage industry, to use this Software subject 
to the following conditions:

1. The Software may not be used for competitive analysis or benchmarking.
2. The Software may not be redistributed, modified, or used to create derivative works.
3. All copyright notices and this permission notice shall be included in all copies.

This Software is provided "AS IS" without warranty of any kind. See Legal Disclaimers 
section for full warranty disclaimer and liability limitations.

For licensing inquiries, please contact: ebarreto@purestorage.com

## Features

- Real-time performance metrics visualization
- Multiple test types support
- Configurable test parameters
- Historical results tracking
- Automatic metric validation
- Interactive graphs for historical data

## Workflow Components

### 1. User Interface (VDBenchUI Class)

#### Test Configuration (Sidebar)
- **Test Type Selection:**
  - Sequential Read
  - Sequential Write
  - Random Read
  - Random Write
  - Mixed Workload

- **Block Size Options:**
  - Ranges from 4K to 1M
  - Available sizes: 4K, 8K, 16K, 32K, 64K, 128K, 256K, 512K, 1M

- **Thread Configuration:**
  - Adjustable from 1 to 64 threads
  - Default: 8 threads

- **Duration Setting:**
  - Range: 10 to 3600 seconds
  - Default: 60 seconds

- **Target Path:**
  - Customizable storage location
  - Automatic directory validation
  - Option to create missing directories

### 2. Test Execution (_run_test method)

#### Real-time Monitoring
- Progress bar showing test completion
- Status text updates
- Live metrics display:
  - IOPS (Input/Output Operations Per Second)
  - Throughput (MB/s)
  - Latency (milliseconds)

#### Metric Validation
The system validates performance metrics using three methods:

1. **Direct Calculation:**
   - Basic IOPS/throughput relationship based on block size

2. **Queue-Depth Adjusted:**
   - Accounts for NVMe queue depth
   - Includes overhead adjustments

3. **Empirical Method:**
   - Uses observed ratios from real-world data
   - Adapts to actual storage behavior

### 3. Results Handling

#### Historical Data
- Results stored in results.json
- Interactive graphs showing:
  - IOPS over time
  - Throughput performance history

#### Performance Analysis
- Detailed logging of test configurations
- Variance analysis of metrics
- Performance validation warnings

## Technical Details

### Metric Calculations

1. **IOPS to Throughput:**
   ```python
   throughput = (iops * block_size_bytes) / (1024 * 1024)  # MB/s
   ```

2. **Throughput to IOPS:**
   ```python
   iops = (throughput * 1024 * 1024) / block_size_bytes
   ```

### Validation Thresholds
- 25% variance allowance for performance metrics
- Automatic queue depth adjustment (max 32)
- NVMe-specific optimizations

## Usage Guide

1. **Starting a Test:**
   - Configure test parameters in sidebar
   - Verify/create target directory
   - Click "Start Test" button

2. **Monitoring Progress:**
   - Watch real-time metrics
   - Monitor progress bar
   - Check validation warnings

3. **Analyzing Results:**
   - Review historical graphs
   - Check logs for detailed analysis
   - Verify metric consistency

## Error Handling

The application includes comprehensive error handling for:
- Invalid directory paths
- Test execution failures
- Metric validation issues
- Data consistency problems

## Dependencies

- Streamlit: Web interface
- Pandas: Data handling
- Plotly: Interactive graphs
- VDBench: Core testing engine

## Best Practices

1. **Test Configuration:**
   - Start with smaller durations for initial tests
   - Verify target directory permissions
   - Consider system resources when setting thread count

2. **Performance Monitoring:**
   - Watch for validation warnings
   - Monitor system resources during tests
   - Check historical trends

3. **Results Analysis:**
   - Compare results across different configurations
   - Verify metric consistency
   - Consider environmental factors

## Troubleshooting

Common issues and solutions:
1. Directory access errors: Check permissions
2. High variance warnings: Verify system load
3. Inconsistent metrics: Check system resources

## Notes

- The tool is optimized for NVMe storage devices
- Performance metrics include overhead adjustments
- Historical data provides trend analysis capabilities

## Installation & Running

### Prerequisites

### 1. Python Environment
- Python 3.7 or higher installed
- pip (Python package installer)
- Git (optional, for cloning repository)

### 2. VDBench Installation
1. **Download VDBench:**
   - Go to Oracle's website: https://www.oracle.com/downloads/server-storage/vdbench-downloads.html
   - Download VDBench (version 50406 or later recommended)
   - Accept the license agreement
   - Save the zip file

2. **Install VDBench:**
   Windows:
   ```cmd
   # Create directory for VDBench
   mkdir C:\vdbench
   
   # Extract the downloaded zip to C:\vdbench
   # Ensure vdbench.bat is in C:\vdbench\vdbench
   ```

   macOS/Linux:
   ```bash
   # Create directory for VDBench
   mkdir -p ~/vdbench
   
   # Extract the downloaded zip
   unzip vdbench*.zip -d ~/vdbench
   
   # Make the script executable
   chmod +x ~/vdbench/vdbench
   ```

3. **Add VDBench to System Path:**
   
   Windows:
   - Open System Properties → Advanced → Environment Variables
   - Under System Variables, find "Path"
   - Click Edit → New
   - Add `C:\vdbench`
   - Click OK to save

   macOS/Linux:
   ```bash
   echo 'export PATH="$HOME/vdbench:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

4. **Verify Installation:**
   ```bash
   vdbench -t
   # Should display VDBench version information
   ```

### 3. Storage Performance Tool Installation

### Installation Steps

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/enrique-purestorage/Pure-Storage-VDBench.git
   cd Pure-Storage-VDBench
   ```

2. **Navigate to the project directory:**
   ```bash
   cd storage-performance-testing-tool
   ```

3. **Install required dependencies:**
   
   Windows:
   ```cmd
   pip install -r requirements.txt
   ```
   
   macOS/Linux:
   ```bash
   pip3 install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit application:**

   Windows:
   ```cmd
   streamlit run vdbench_ui.py
   ```
   
   macOS/Linux:
   ```bash
   streamlit run vdbench_ui.py
   ```

2. **Access the application:**
   - The application will automatically open in your default web browser
   - If it doesn't open automatically, navigate to the URL shown in the terminal (typically http://localhost:8501)

### Troubleshooting Installation

If you encounter permission errors:

Windows:
```cmd
pip install --user -r requirements.txt
```

macOS/Linux:
```bash
pip3 install --user -r requirements.txt
# OR
sudo pip3 install -r requirements.txt
```

If streamlit is not recognized as a command:
```bash
python -m streamlit run vdbench_ui.py
# OR
python3 -m streamlit run vdbench_ui.py
```

### Streamlit Server Configuration

#### Windows Server Specific Setup
1. **Create Streamlit Configuration:**
   ```cmd
   mkdir %USERPROFILE%\.streamlit
   notepad %USERPROFILE%\.streamlit\config.toml
   ```

2. **Add these configurations to config.toml:**
   ```toml
   [server]
   address = "0.0.0.0"  # Allows external connections
   port = 8501          # Default port, can be changed
   maxUploadSize = 200  # In MB
   enableXsrfProtection = true
   enableCORS = false   # Enable if needed for cross-origin requests

   [browser]
   serverAddress = "your_windows_server_ip"  # Replace with actual IP
   serverPort = 8501
   ```

3. **Firewall Configuration:**
   ```cmd
   netsh advfirewall firewall add rule name="Streamlit" dir=in action=allow protocol=TCP localport=8501
   ```

4. **Running as a Service (Optional):**
   Create a batch file (start_streamlit.bat):
   ```batch
   @echo off
   call C:\path\to\venv\Scripts\activate.bat
   streamlit run C:\path\to\vdbench_ui.py --server.address 0.0.0.0 --server.port 8501
   ```

#### Accessing the Application
- Local: http://localhost:8501
- Remote: http://your_windows_server_ip:8501
- Use fully qualified domain name if available

#### Security Considerations
- Use Windows authentication when possible
- Consider running behind a reverse proxy
- Implement SSL/TLS if exposed to external networks
- Review firewall rules regularly