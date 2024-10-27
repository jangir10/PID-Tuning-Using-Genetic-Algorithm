# PID Parameters Generator Using Genetic Algorithm

## The Notebook:
The notebook contains the code for the PID parameters generator using Genetic Algorithm for an example test case.

# PID Tuning Web Application

A web-based application that calculates PID (Proportional-Integral-Derivative) controller parameters from transfer function coefficients. This tool provides a simple interface for control systems engineers and students to quickly obtain PID tuning parameters.

## Features

- Simple web interface for input of transfer function coefficients
- Real-time calculation of PID parameters (Kp, Ki, Kd)
- Support for various order transfer functions
- Input validation and error handling
- Responsive design
- Loading states and clear feedback

## Prerequisites

Before running the application, ensure you have Python installed on your system. The application requires the following Python packages:

```bash
pip install flask numpy scipy control
```

## Project Structure

```
pid-tuning-app/
├── app.py              # Flask backend application
├── templates/          # Frontend templates directory
│   └── index.html     # Main web interface
└── README.md          # This file
```

## Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
# or create the directory structure manually
```

2. Install the required Python packages:
```bash
pip install flask numpy scipy control
```

## Running the Application

1. Navigate to the project directory:
```bash
cd pid-tuning-app
```

2. Start the Flask server:
```bash
python app.py
```

3. Open your web browser and go to:
```
http://localhost:5000
```

## Usage

1. Enter the transfer function coefficients:
   - Numerator coefficients: Enter comma-separated values (e.g., "1" or "1,2")
   - Denominator coefficients: Enter comma-separated values (e.g., "1,2,1")

2. Example inputs:
   - First-order system:
     - Numerator: 1
     - Denominator: 1,1
   
   - Second-order system:
     - Numerator: 1
     - Denominator: 1,2,1
   
   - Third-order system:
     - Numerator: 1,2
     - Denominator: 1,3,3,1

3. Click "Calculate PID Parameters" to get the results

## Technical Details

### Backend (app.py)
- Built with Flask
- Uses control systems library for transfer function handling
- Implements PID tuning rules based on pole placement
- Provides JSON API endpoint for calculations

### Frontend (index.html)
- Pure HTML/CSS/JavaScript implementation
- Responsive design for various screen sizes
- Real-time input validation
- Clear error messaging and loading states

## Error Handling

The application handles various error cases:
- Invalid input formats
- Empty inputs
- Network connection issues
- Backend calculation errors
- Server connection problems

## Limitations

- Assumes linear time-invariant systems
- Basic PID tuning rules implemented
- Limited to stable systems
- No system response visualization (yet)

## Future Improvements

Potential areas for enhancement:
- Add system response visualization
- Support for more complex transfer functions
- Additional tuning methods
- Export functionality for parameters
- System stability analysis
- Batch processing capability

## Troubleshooting

Common issues and solutions:

1. "Template not found" error:
   - Ensure the `templates` folder exists
   - Check that `index.html` is in the correct location
   - Verify folder and file names are lowercase

2. Connection errors:
   - Confirm Flask server is running
   - Check you're accessing through `http://localhost:5000`
   - Don't open the HTML file directly

3. Calculation errors:
   - Verify input format (comma-separated numbers)
   - Check denominator's leading coefficient is not zero
   - Ensure transfer function is proper

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.


