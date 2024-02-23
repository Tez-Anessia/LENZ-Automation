import logging

def setUp(logFile='automationReport.log'):
    # Create logger
    logger = logging.getLogger('automationLogger')
    # Check if handlers already exist to prevent duplication
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # global logging level
        
        # -------Create file handler & set level to debug -------
        fileHandler = logging.FileHandler(logFile)
        fileHandler.setLevel(logging.DEBUG)
        
        # -------formatter-------
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        
        # -------Add handler to logger-------
        logger.addHandler(fileHandler)
    
    return logger

# -------summary for end report results-------
def generateReport(logFile='automationReport.log'):
    summaryReport = []
    with open(logFile, 'r') as file:
        for line in file:
            if 'INFO' in line:
                summaryReport.append(line.strip())
    return summaryReport
