"""Main module for the IdentiFile API.

This module defines the FastAPI application and routes.

Copyright (C) 2023 IdentiFile Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import logging
from typing import Dict, Any

import src.api.version
import src.api.identify
from src.api.errors import (
    FileProcessingError,
    FileTypeError,
    FileSizeError,
    MissingFileError,
    create_error_response,
)
from fastapi import FastAPI, UploadFile, File, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("identifile")

# Create FastAPI app
app = FastAPI(
    title="IdentiFile API",
    description="REST API for identifying file types based on content using Google Magika AI or standard file header detection.",
    version=src.api.version.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# Exception handlers
@app.exception_handler(FileProcessingError)
async def file_processing_error_handler(
    request: Request, exc: FileProcessingError
) -> JSONResponse:
    """Handle file processing errors."""
    logger.error(f"File processing error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=create_error_response(
            exc.status_code, exc.detail, error_type="FileProcessingError"
        ),
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Handle HTTP exceptions."""
    logger.error(f"HTTP error: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=create_error_response(
            exc.status_code, exc.detail, error_type="HTTPException"
        ),
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle general exceptions."""
    logger.error(f"Unexpected error: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=create_error_response(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "An unexpected error occurred",
            error_type="InternalServerError",
        ),
    )


# Routes
@app.get("/version", response_model=Dict[str, Any])
def version():
    """Get API version information."""
    logger.info("Version endpoint called")
    return src.api.version.version()


@app.post("/identify")
def identify(file: UploadFile = File(...)):
    """Identify file using standard header detection."""
    if not file:
        raise MissingFileError()

    logger.info(f"Identifying file: {file.filename} using standard method")
    return src.api.identify.identify(file)


@app.post("/ai_identify")
def ai_identify(file: UploadFile = File(...)):
    """Identify file using Google Magika AI."""
    if not file:
        raise MissingFileError()

    logger.info(f"Identifying file: {file.filename} using AI method")
    return src.api.identify.ai_identify(file)
