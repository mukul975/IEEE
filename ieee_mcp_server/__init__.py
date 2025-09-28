"""
IEEE Model Context Protocol Server

A comprehensive MCP server providing 15 tools for IEEE academic research,
standards management, citation formatting, and conference operations.
"""

__version__ = "0.1.0"
__author__ = "IEEE MCP Server Team"
__email__ = "ieee-mcp@example.com"
__description__ = "IEEE MCP server with 15 comprehensive academic research tools"

from .server import app

__all__ = ["app", "__version__"]